#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/website/admin.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.
import os
import codecs
import shutil
import csv
import json
import hashlib

from pymongo import MongoClient
from functools import wraps
from cStringIO import StringIO

from flask import (Blueprint, render_template, request, g, flash, redirect,
                   url_for, send_file, make_response)
from flask.ext.babel import gettext as _
from flask.ext.babel import get_locale, to_user_timezone, lazy_gettext
from flask.ext.login import login_fresh, current_user
from sqlalchemy import func
from railgun.common.hw import Homework
from sqlalchemy.orm import contains_eager
from werkzeug.exceptions import NotFound

from .archivefile import unzip
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
from railgun.runner.context import app as runner_app
from .context import app, db
from .models import User, Handin, FinalScore, Vote, VoteItem, assign_values
from .forms import AdminUserEditForm, CreateUserForm, VoteJsonEditForm,AddproblemForm,Problem_edit_Form,AddcourseForm,Course_Choose_Form
from .userauth import auth_providers,list_to_str
from .credential import login_manager
from .navibar import navigates, NaviItem
from .utility import round_score, group_histogram
from .codelang import languages
from config import HOMEWORK_DIR,HOMEWORK_DIR_FOR_CLASS
from config import HOMEWORK_TYPE_SET
from pymongo import MongoClient
from .hw import HwProxy
from .i18n import get_best_locale_name
from cStringIO import StringIO
from railgun.maintain.hwcache import HwCacheTask
import railgun.runner.hw


#: A :class:`~flask.Blueprint` object.  All the views for administration
#: are registered to this blueprint.
bp = Blueprint('admin', __name__)

def admin_required(method):
    """A decorator on Flask view functions that validate whether the request
    user is an administrator.

    If not authenticated, the request user will be redirected to
    :func:`~railgun.website.views.signin`.
    If not an administrator, an error message will be flashed and the
    request user will be redirected to :class:`~railgun.website.views.index`.
    If the session is stale, the request user will be redirected to
    :func:`~railgun.website.views.reauthenticate`.

    Usage::

        @bp.route('/')
        @admin_required
        def admin_index():
            return 'This page can only be accessed by admins.'
    """
    @wraps(method)
    def inner(*args, **kwargs):
        if not current_user.is_authenticated():
            return login_manager.unauthorized()
        if not current_user.is_admin:
            flash(_("Only admin can view this page!"), 'danger')
            return redirect(url_for('index'))
        if not login_fresh():
            return login_manager.needs_refresh()
        return method(*args, **kwargs)
    return inner


@bp.route('/users/')
@admin_required
def users():
    """Admin page to manage registered users.
    Information of the users will be gathered on this page, and each record
    will be given a link to its editing page.

    This page supports page navigation, thus accepts `page` and `perpage`
    query string argument, where `page` defines the navigated page id
    (>= 1), and `perpage` defines the page size (default 10).

    :route: /admin/users/
    :method: GET
    :template: admin.users.html
    """
    # get pagination argument
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    try:
        perpage = int(request.args.get('perpage', 10))
    except ValueError:
        perpage = 10
    # query about all users
    users = User.query.filter()
    # build pagination object
    return render_template(
        'admin.users.html',
        the_page=users.paginate(page, perpage)
    )


@bp.route('/problems/')
@admin_required
def problems():
    '''get pagination argument query about all problems '''
    problems = app.config['PROBLEM_COLLECTION'].find()
    problem_dict = {}
    for type in app.config['HOMEWORK_TYPE_SET']:
        problem_dict.update({type:[]})
    for problem in problems:
        problem_dict[problem['type']].append(problem)
    course_name = "Global"
    return render_template(
                           'admin.problems.html',
                           problem_dict = problem_dict,
                           course_name = course_name
                           )


@bp.route('/courses/')
@admin_required
def courses():
    '''get the information of all courses for railgun'''
    courses = app.config['COURSE_COLLECTION'].find()
    course_dict = {}
    for course in courses:
        course_dict.update({course['name']:""})
        problem_list = str(course['problem_list']).split('@')
        for problem in problem_list:
            if len(problem) == 0:
                continue
            mongo_problem = app.config['PROBLEM_COLLECTION'].find_one({"name":problem})
            course_dict[course['name']] += mongo_problem['ch_name'] + " , "
        course_dict[course['name']] = course_dict[course['name']][:-2]

    return render_template('admin.courses.html',course_dict = course_dict)

@bp.route('/course/<name>/delete')
@admin_required
def course_delete(name):
    """ Delete the given course
        
        delete the course in the mongodb
        delete the file folder
        """
    
    next = request.args.get('next')
    #delete the course in mongodb
    if app.config['COURSE_COLLECTION'].count({"name": name}) > 0:
        app.config['COURSE_COLLECTION'].remove({"name": name})
    
    #delete the file folder
    if not os.path.isdir(app.config['HOMEWORK_DIR_FOR_CLASS']):
        os.mkdir(app.config['HOMEWORK_DIR_FOR_CLASS'])
    
    course_path = os.path.join(app.config['HOMEWORK_DIR_FOR_CLASS'],name)

    if os.path.isdir(course_path):
        shutil.rmtree(course_path)
    
    flash(_('The course has been deleted.'), 'success')
    return redirect(next or url_for('.courses'))


@bp.route('/adduser/', methods=['GET', 'POST'])
@admin_required
def adduser():
    """Admin page to create a new user.

    The new users will have ``<username>@<config.EXAMPLE_USER_EMAIL_SUFFIX>``
    as their initial email address.  The system will require such users to
    fill in their real emails address when they log in for the first time.

    If the user has been created successfully, the visitor will be redirected
    to :func:`~railgun.website.admin.users`.

    :route: /admin/adduser/
    :method: GET, POST
    :form: :class:`~railgun.website.forms.CreateUserForm`
    :template: admin.adduser.html
    """
    form = CreateUserForm()
    if form.validate_on_submit():
        # Construct user data object
        user = User()
        form.populate_obj(user)
        user.email = user.name + app.config['EXAMPLE_USER_EMAIL_SUFFIX']
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            dictionary = {}
            app.config['USERS_COLLECTION'].insert({"_id":user.name,"password":user.password,"problem_list":dictionary})
            return redirect(url_for('.users'))
        except Exception:
            app.logger.exception('Cannot create account %s' % user.name)
        flash(_("I'm sorry but we may have met some trouble. Please try "
                "again."), 'warning')
    return render_template('admin.adduser.html', form=form)



@bp.route('/addcourse/', methods=['GET', 'POST'])
@admin_required
def addcourse():
    form = AddcourseForm()
    if form.validate_on_submit():
        if app.config['COURSE_COLLECTION'].count({"name":form.name.data}) != 0:
            flash(_("The course name you input has already been occupied.Please try again."))
        else:
            if not os.path.isdir(HOMEWORK_DIR_FOR_CLASS):
                os.mkdir(HOMEWORK_DIR_FOR_CLASS)
            course_path = os.path.join(HOMEWORK_DIR_FOR_CLASS,form.name.data)
            if not os.path.isdir(course_path):
                os.mkdir(course_path)
            app.config['COURSE_COLLECTION'].insert({"name":form.name.data,"path":course_path,"problem_list":""})
            flash(_("Insert Course successfully!"),'success')
            return redirect(url_for('.courses'))
    return render_template('admin.addcourse.html',form = form)

@bp.route('/course/<slug>/',methods=['GET','POST'])
@admin_required
def course_edit(slug):
    course = app.config['COURSE_COLLECTION'].find_one({"name": slug})
    course_problem_list = str(course['problem_list']).split('@')
    problems = app.config['PROBLEM_COLLECTION'].find()

    problem_dict = {}
    for type in app.config['HOMEWORK_TYPE_SET']:
        problem_dict.update({type:[]})
    for problem in problems:
        problem_dict[problem['type']].append(problem)

    return render_template('admin.course_edit.html',problem_dict = problem_dict,problem_list = course_problem_list,course_name = slug)

def xml_for_problem(slug,time,course):
    """
        this function can handle the situation that xml file does not exist automatically
        """
    mongo_homework = MongoClient()["railgun"].problem.find_one({"name": slug})
    if mongo_homework is None:
        return
    homework_path = str(mongo_homework['path'])
    if course != "Global":
        mongo_course = app.config['COURSE_COLLECTION'].find_one({"name": course})
        homework_path = os.path.join(mongo_course['path'],mongo_homework['type'],mongo_homework['name'])
    xml_homework_path = os.path.join(homework_path,'hw.xml')
    m = hashlib.md5()
    hashstr = slug
    if course != "Global":
        hashstr = hashstr + course
    hashstr = hashstr.encode('utf-16')
    m.update(hashstr)
    hashcode = m.hexdigest()
    f = codecs.open(xml_homework_path,'w','utf-8')
    content = '<?xml version="1.0"?>\n<homework>\n' + '<uuid>' + hashcode + '</uuid>\n'
    cname = mongo_homework['ch_name']
    ename = slug
    content = content + '<names>\n<name lang="zh-cn">' + cname +'</name>\n <name lang="en">' + ename + '</name>\n</names>\n'
    content = content + '<deadlines>\n'
    content = content + '<due>\n<timezone>Asia/Shanghai</timezone>\n<date>' + str(time[0]) +' 23:59:59'+ '</date>\n<scale>1.0</scale>\n' + '</due>\n'
    content = content + '<due>\n<timezone>Asia/Shanghai</timezone>\n<date>' + str(time[1]) +' 23:59:59'+ '</date>\n<scale>0.75</scale>\n' + '</due>\n'
    content = content + '<due>\n<timezone>Asia/Shanghai</timezone>\n<date>' + str(time[2]) +' 23:59:59'+ '</date>\n<scale>0.5</scale>\n' + '</due>\n'
    content = content + '<due>\n<timezone>Asia/Shanghai</timezone>\n<date>' + str(time[3]) +' 23:59:59'+ '</date>\n<scale>0.0</scale>\n' + '</due>\n'
    content = content + '</deadlines>\n<files />\n</homework>'
    f.write(content)
    f.close()


@bp.route('/addproblem/', methods=['GET', 'POST'])
@admin_required
def addproblem():
    form = AddproblemForm()
    if form.validate_on_submit():
        # find in mongo db
        if app.config['PROBLEM_COLLECTION'].count({"name":form.name.data}) != 0:
            flash(_("I'm sorry but the homework name in English you input has already in Homework Set. Please try again."), 'warning')
        elif app.config['PROBLEM_COLLECTION'].count({"ch_name":form.ch_name.data}) != 0:
            flash(_("I'm sorry but the homework name in Chinese you input has already in Homework Set. Please try again."), 'warning')
        elif form.type.data not in HOMEWORK_TYPE_SET:
            flash(_("I'm sorry but the homework type you input is illegal. Please try "
                    "again."), 'warning')
        else:
            homework_path = os.path.join(HOMEWORK_DIR,form.type.data,form.name.data)
            app.config['PROBLEM_COLLECTION'].insert({"name":form.name.data,"ch_name":form.ch_name.data,"path":homework_path,"type":form.type.data,"desc":form.word_desc.data})
            code_homework_path = os.path.join(homework_path,'code')
            desc_homework_path = os.path.join(homework_path,'desc')
            solve_homework_path = os.path.join(homework_path,'solve')
            #create the type file folder and the problem_name file folder
            if not os.path.isdir(os.path.join(HOMEWORK_DIR,form.type.data)):
                os.mkdir(os.path.join(HOMEWORK_DIR,form.type.data))
            if not os.path.isdir(homework_path):
                os.mkdir(homework_path)
            #try to create file folder .code .desc .solve
            #.code
            if os.path.isdir(code_homework_path):
                shutil.rmtree(code_homework_path)
            form.code_file.data.save(os.path.join(homework_path,'tmp'))
            unzip(os.path.join(homework_path,'tmp'),homework_path)
            os.remove(os.path.join(homework_path,'tmp'))
            #.desc .solve
            if not os.path.isdir(desc_homework_path):
                os.mkdir(desc_homework_path)
            if not os.path.isdir(solve_homework_path):
                os.mkdir(solve_homework_path)
            timestr = str(g.utcnow.year) + "-" + str(g.utcnow.month) + "-" + str(g.utcnow.day)
            #try to create file desc/zh-cn.md desc/en.md solve/en.md desc/zh-cn.md
            desc_zh = os.path.join(desc_homework_path,'zh-cn.md')
            desc_en = os.path.join(desc_homework_path,'en.md')
            solve_zh = os.path.join(solve_homework_path,'zh-cn.md')
            solve_en = os.path.join(solve_homework_path,'en.md')
            file_name = [desc_en,desc_zh,solve_en,solve_zh]
            for file in file_name:
                if not os.path.isfile(file):
                    f = codecs.open(file,'w','utf-8')
                    f.close()
            #try to create file .hw.xml
            time = [timestr,timestr,timestr,timestr]
            xml_for_problem(form.name.data,time,"Global")
            flash(_("Insert Homework successfully!"),'success')
            
            task = HwCacheTask(logstream=StringIO())
            task.excute_single(homework_path,form.name.data)
            return redirect(url_for('.problems'))
    return render_template('admin.addproblem.html', form=form)


class test_obj:
    desc = _('Edit description here')
    solve = _('Edit solve here')



@bp.route('/problem/<slug>/<course>/',methods=['GET','POST'])
@admin_required
def problem_edit(slug,course):
    test = test_obj()
    mongo_homework = MongoClient()["railgun"].problem.find_one({"name": slug})
    homework_path = str(mongo_homework['path'])
    
    if course != "Global":
        mongo_course = app.config['COURSE_COLLECTION'].find_one({"name": course})
        homework_path = os.path.join(mongo_course['path'],mongo_homework['type'],mongo_homework['name'])

    hw1 = Homework()
    hw = HwProxy(hw1.load(homework_path))

    solve_folder_path = os.path.join(homework_path,'solve')
    desc_folder_path = os.path.join(homework_path,'desc')
    code_folder_path = os.path.join(homework_path,'code')

    locale = get_best_locale_name(['zh-cn', 'en'])
    locale_md = locale + '.md'

    solve_file_path = os.path.join(homework_path,'solve',locale_md)
    desc_file_path = os.path.join(homework_path,'desc',locale_md)
    
    homework_set = os.listdir(homework_path)

    #create .solve .desc .code
    if os.path.isdir(solve_folder_path) == False:
        os.mkdir(solve_folder_path)

    if os.path.isdir(desc_folder_path) == False:
        os.mkdir(desc_folder_path)

    if os.path.isdir(code_folder_path) == False:
        os.mkdir(code_folder_path)

    if os.path.isfile(solve_file_path):
        solve_file_object = codecs.open(solve_file_path,'r','utf-8')
        test.solve = solve_file_object.read()
        solve_file_object.close()
    else:
        solve_file_object = open(solve_file_object,'w')
    

    if os.path.isfile(desc_file_path):
        desc_file_object = codecs.open(desc_file_path,'r','utf-8')
        test.desc = desc_file_object.read()
        desc_file_object.close()
    else:
        desc_file_object = open(desc_file_object,'w')


    form = Problem_edit_Form(obj = test)
    if not hw:
        raise NotFound()
    hwlangs = hw.get_code_languages()

    forms = {
        k: languages[k].upload_form(hw) for k in hwlangs
    }
    
    if form.validate_on_submit():
        if hw.count_attach() > 0:
            heading = request.files['heading']
            if heading.filename is not u'':
                upload_path = os.path.join(app.config['HOMEWORK_PACK_DIR'],slug)
                heading.save(os.path.join(upload_path,heading.filename))
        time = []
        time.append(request.form['ddl1.0'])
        time.append(request.form['ddl0.75'])
        time.append(request.form['ddl0.5'])
        time.append(request.form['ddl0.0'])
        for i in [0,1,2,3]:
            str_time = str(hw.deadlines[i][0]).split(' ')[0]
            if time[i] == '':
                time[i] = str_time
        solve_file_object = codecs.open(solve_file_path,'w','utf-8')
        solve_file_object.write(form.solve.data)
        solve_file_object.close()
        desc_file_object = codecs.open(desc_file_path,'w','utf-8')
        desc_file_object.write(form.desc.data)
        desc_file_object.close()
        xml_for_problem(slug,time,course)
        if course != "Global":
            m = hashlib.md5()
            hashstr = slug + course
            hashstr = hashstr.encode('utf-16')
            m.update(hashstr)
            hashcode = m.hexdigest()
            railgun.runner.hw.update_homework.delay(hashcode,homework_path)
    return render_template('admin.homework_edit.html',homework = mongo_homework, form=form,hw = hw,hwlangs = hwlangs,course = course)

@bp.route('/problems/<name>/delete/')
@admin_required
def problem_delete(name):
    """Delete the given user.
        
        This view accepts an extra query string argument `next`, where the visitor
        will be redirected to `next` after the operation.  If `next` is not given,
        the visitor will be redirected to :func:`~railgun.website.admin.problems`.
        
        .. note::
        
        An administrator cannot delete him or herself.
        
        :route: /admin/problems/<name>/delete/
        :method: GET
        
        :param name: The name of operated user.
        :type name: :class:`str`
        """
    next = request.args.get('next')
    homework = MongoClient()["railgun"].problem.find_one({"name": name})
    if homework == None:
        flash(_("Can't find the item"),'warning')
        return redirect(next or url_for('.problems'))
    if os.path.isdir(homework["path"]):
        shutil.rmtree(homework["path"])
    MongoClient()["railgun"].problem.remove({"name": name})
    flash(_("Delete this homework successfully",'success'))
    return redirect(next or url_for('.problems'))

@bp.route('/users/<name>/', methods=['GET', 'POST'])
@admin_required
def user_edit(name):
    """Admin page to modify an existing user.

    For the accounts from third-party authentication providers, some fields
    of the form may be locked and cannot be modified.  This feature isn't
    implemented here, but in :mod:`railgun.website.userauth`.

    If the user has been successfully updated, the visitor will be redirected
    to :func:`~railgun.website.admin.users`.

    :route: /admin/users/<name>/
    :method: GET, POST
    :form: :class:`~railgun.website.forms.AdminUserEditForm`
    :template: admin.user_edit.html
    """
    # Profile edit should use typeahead.js
    g.scripts.deps('typeahead.js')

    # Get the user object
    the_user = User.query.filter(User.name == name).one()

    # Create the profile form.
    # Note that some fields cannot be edited in certain auth providers,
    # which should be stripped from schema.'
    
    form = AdminUserEditForm(obj = the_user)
    if the_user.provider:
        auth_providers.init_form(the_user.provider, form)
    form.the_user = the_user

    if form.validate_on_submit():
        # Set password if passwd field exists
        if 'password' in form:
            pwd = form.password.data
            if pwd:
                the_user.set_password(pwd)
            del form['password']
            del form['confirm']
        else:
            pwd = None

        # Copy values into current_user object
        form.populate_obj(the_user)

        # Commit to main database and auth provider
        try:
            if the_user.provider:
                auth_providers.push(the_user, pwd)
            db.session.commit()
            flash(_('Profile saved.'), 'info')
        except Exception:
            app.logger.exception('Cannot update account %s' % the_user.name)
            flash(_("I'm sorry but we may have met some trouble. Please try "
                    "again."), 'warning')
        return redirect(url_for('admin.users'))

    # Clear password & confirm here is ok.
    if 'password' in form:
        form.password.data = None
        form.confirm.data = None
    
    return render_template(
        'admin.user_edit.html',
        locale_name=str(get_locale()),
        form=form,
        the_user=the_user,
    )


@bp.route('/users/<name>/activate/')
@admin_required
def user_activate(name):
    """Activate the given user.

    This view accepts an extra query string argument `next`, where the visitor
    will be redirected to `next` after the operation.  If `next` is not given,
    the visitor will be redirected to :func:`~railgun.website.admin.users`.

    :route: /admin/users/<name>/activate/
    :method: GET

    :param name: The name of operated user.
    :type name: :class:`str`
    """
    next = request.args.get('next')
    the_user = User.query.filter(User.name == name).one()
    the_user.is_active = True
    db.session.commit()
    flash(_('User activated.'), 'success')
    return redirect(next or url_for('.users'))

@bp.route('/courses/<name>/<p_name>/delete')
@admin_required
def course_delete_problem(name,p_name):
    next = request.args.get('next')
    if app.config['COURSE_COLLECTION'].count({"name": name}) != 0 and app.config['PROBLEM_COLLECTION'].count({"name": p_name}) != 0:
        course = app.config['COURSE_COLLECTION'].find_one({"name": name})
        homework = app.config['PROBLEM_COLLECTION'].find_one({"name":p_name})
        course_problem_list_str = str(course['problem_list'])
        course_problem_list_list = course_problem_list_str.split('@')
        new_list = []
        #check whether the p_name in the problem_list
        if p_name in course_problem_list_list:
            for item in course_problem_list_list:
                if item != p_name:
                    new_list.append(item)
            new_str = list_to_str(new_list)
            # update the mongodb
            app.config['COURSE_COLLECTION'].remove({"name": name})
            app.config['COURSE_COLLECTION'].insert({"name":course['name'],"path":course['path'],"problem_list":new_str})
            # update the file system
            problem_path = os.path.join(course['path'],homework['type'],p_name)
            if os.path.isdir(os.path.join(course['path'],homework['type'])):
                if p_name in os.listdir(os.path.join(course['path'],homework['type'])):
                    m = hashlib.md5()
                    hashstr = p_name + name
                    hashstr = hashstr.encode('utf-16')
                    m.update(hashstr)
                    hashcode = m.hexdigest()
                    railgun.runner.hw.delete_homework.delay(hashcode)
                    shutil.rmtree(problem_path)
                    flash(_('Delete successfully.'), 'success')
            else:
                flash(_("Can't delete this homework!"), 'warning')
        else:
            flash(_("Can't delete this homework!"), 'warning')
    else:
        flash(_("Can't delete this homework!"), 'warning')
    return redirect(next or url_for('.courses'))

@bp.route('/courses/<name>/<p_name>/add')
@admin_required
def course_add_problem(name,p_name):
    """add problem p_name to the course's problem list"""
    next = request.args.get('next')
    if app.config['COURSE_COLLECTION'].count({"name": name}) != 0 and app.config['PROBLEM_COLLECTION'].count({"name": p_name}) != 0:
        course = app.config['COURSE_COLLECTION'].find_one({"name": name})
        homework = app.config['PROBLEM_COLLECTION'].find_one({"name":p_name})
        course_problem_list_str = str(course['problem_list'])
        course_problem_list_list = course_problem_list_str.split('@')
        #check whether the p_name in the problem list
        if p_name not in course_problem_list_list:
            if course_problem_list_str == "":
                course_problem_list_str = p_name
            else:
                course_problem_list_str = course_problem_list_str + "@" + p_name
            app.config['COURSE_COLLECTION'].remove({"name": name})
            app.config['COURSE_COLLECTION'].insert({"name":course['name'],"path":course['path'],"problem_list":course_problem_list_str})
            course_path = os.path.join(course['path'],homework['type'])
            type_set = os.listdir(course['path'])
            #make sure the homework_type does not exist
            if homework['type'] not in type_set:
                os.mkdir(course_path)
            course_path_problem_path = os.path.join(course_path,p_name)
            course_path_problem_path_desc = os.path.join(course_path_problem_path,'desc')
            course_path_problem_path_solve = os.path.join(course_path_problem_path,'solve')
            course_path_problem_path_code = os.path.join(course_path_problem_path,'code')
            #make sure the p_name does not exist
            if p_name not in os.listdir(course_path):
                os.mkdir(course_path_problem_path)
            shutil.copy(os.path.join(homework['path'],'hw.xml'),course_path_problem_path)
            if 'desc' in os.listdir(course_path_problem_path):
                shutil.rmtree(course_path_problem_path_desc)
            if 'solve' in os.listdir(course_path_problem_path):
                shutil.rmtree(course_path_problem_path_solve)
            if 'code' in os.listdir(course_path_problem_path):
                shutil.rmtree(course_path_problem_path_code)
            #make sure .solve and .desc not exist now
            shutil.copytree(os.path.join(homework['path'],'desc'),course_path_problem_path_desc)
            shutil.copytree(os.path.join(homework['path'],'solve'),course_path_problem_path_solve)
            shutil.copytree(os.path.join(homework['path'],'code'),course_path_problem_path_code)
            hw1 = Homework()
            hw = HwProxy(hw1.load(course_path_problem_path))
            time = []
            for i in [0,1,2,3]:
                str_time = str(hw.deadlines[i][0]).split(' ')[0]
                time.append(str_time)
            xml_for_problem(p_name,time,name)
            m = hashlib.md5()
            hashstr = p_name + name
            hashstr = hashstr.encode('utf-16')
            m.update(hashstr)
            hashcode = m.hexdigest()
            railgun.runner.hw.add_homework.delay(course_path_problem_path)
            flash(_('Add successfully.'), 'success')
        else:
            flash(_("Can't add this homework!"), 'warning')
    else:
        flash(_("Can't add this homework!"), 'warning')
    return redirect(next or url_for('.courses'))

@bp.route('/users/<name>/deactivate/')
@admin_required
def user_deactivate(name):
    """Deactivate the given user.

    This view accepts an extra query string argument `next`, where the visitor
    will be redirected to `next` after the operation.  If `next` is not given,
    the visitor will be redirected to :func:`~railgun.website.admin.users`.

    .. note::

        An administrator cannot deactivate him or herself.

    :route: /admin/users/<name>/deactivate/
    :method: GET

    :param name: The name of operated user.
    :type name: :class:`str`
    """
    next = request.args.get('next')
    the_user = User.query.filter(User.name == name).one()
    # should not allow the user to deactivate himself!
    if the_user.id == current_user.id:
        flash(_('You cannot deactivate yourself!'), 'warning')
    else:
        the_user.is_active = False
        db.session.commit()
        flash(_('User deactivated.'), 'warning')
    return redirect(next or url_for('.users'))


@bp.route('/users/<name>/delete/')
@admin_required
def user_delete(name):
    """Delete the given user.

    This view accepts an extra query string argument `next`, where the visitor
    will be redirected to `next` after the operation.  If `next` is not given,
    the visitor will be redirected to :func:`~railgun.website.admin.users`.

    .. note::

        An administrator cannot delete him or herself.

    :route: /admin/users/<name>/delete/
    :method: GET

    :param name: The name of operated user.
    :type name: :class:`str`
    """
    next = request.args.get('next')
    the_user = User.query.filter(User.name == name).one()
    # should not allow the user to delete himself!
    if the_user.id == current_user.id:
        flash(_('You cannot delete yourself!'), 'warning')
    else:
        # Delete all top scores of this user
        FinalScore.query.filter(FinalScore.user_id == the_user.id).delete()
        # Delete all submissions of this user
        Handin.query.filter(Handin.user_id == the_user.id).delete()
        # Delete this user
        User.query.filter(User.id == the_user.id).delete()
        # commit the changes
        db.session.commit()
        # show messages
        if app.config['USERS_COLLECTION'].count({"_id":name}) > 0:
            app.config['USERS_COLLECTION'].remove({"_id":name})
        flash(_('User deleted.'), 'warning')
    return redirect(next or url_for('.users'))


def _show_handins(username=None):
    """Render an administrator page to show submissions.

    :param user: The interested user's name. If not given, show submissions
        from all users.
    :type user: :class:`str`
    :return: A :class:`flask.Response` object.
    """
    # get pagination argument
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    try:
        perpage = int(request.args.get('perpage', 10))
    except ValueError:
        perpage = 10
    # query about all handins
    handins = Handin.query.join(Handin.user). \
        options(contains_eager(Handin.user)).filter()
    # whether we want to view the submissions from one single user?
    if username:
        user = User.query.filter(User.name == username).first()
        if not user:
            raise NotFound()
        handins = handins.filter(Handin.user_id == user.id)
    # Sort the handins
    handins = handins.order_by(-Handin.id)
    # build pagination object
    return render_template(
        'admin.handins.html', the_page=handins.paginate(page, perpage),
        username=username
    )


@bp.route('/handin/')
@admin_required
def handins():
    """The admin page to show all submissions.

    This page supports page navigation, thus accepts `page` and `perpage`
    query string argument, where `page` defines the navigated page id
    (>= 1), and `perpage` defines the page size (default 10).

    :route: /admin/handin/
    :method: GET
    :template: admin.handins.html
    """
    return _show_handins(None)


@bp.route('/handin/<username>/')
@admin_required
def handins_for_user(username):
    """The admin page to show all submissions from a given user.

    This page supports page navigation, thus accepts `page` and `perpage`
    query string argument, where `page` defines the navigated page id
    (>= 1), and `perpage` defines the page size (default 10).

    :route: /admin/handin/<username>/
    :method: GET
    :template: admin.handins.html

    :param username: The name of queried user.
    :type username: :class:`str`
    """
    return _show_handins(username)


@bp.route('/runqueue/rerun/<handid>/')
@admin_required
def runqueue_rerun(handid):
    """Reset the state of given submission and put it into runqueue again.
    This operation is only enabled if `config.STORE_UPLOAD` is turned on.

    If the operation is successful, the visitor will be redirected to
    the query string argument `next`, or :func:`~railgun.website.admin.handins`
    if `next` is not given.

    :route: /admin/runqueue/rerun/<handid>/
    :method: GET

    :param handid: The uuid of submission.
    :type handid: :class:`str`
    """
    nexturl = request.args.get('next') or url_for('.handins')
    fullscale = request.args.get('fullscale', False)

    # Query about the handin record
    handin = Handin.query.filter(Handin.uuid == handid)
    handin = handin.first()

    # If not found, result 404
    if not handin:
        return _('Submission not found'), 404

    # Get the homework
    hw = g.homeworks.get_by_uuid(handin.hwid)

    # Now reput the submission into runqueue
    if not languages[handin.lang].rerun(handid, hw, fullscale):
        flash(_('The original submission is not stored.'), 'danger')
    else:
        flash(_('Successfully reput the submission into queue!'), 'success')

    return redirect(nexturl)


@bp.route('/runqueue/clear/')
@admin_required
def runqueue_clear():
    """Stop the runner queue, set the score of all pending and running
    submissions to 0.0, and the state to `Rejected`.
    The visitor will be redirected to :func:`~railgun.website.admin.handins`
    after the operation takes place.

    :route: /admin/runqueue/clear/
    :method: GET
    """

    # We must not use flask.ext.babel.lazy_gettext, because we'll going to
    # store it in the database!
    from railgun.common.lazy_i18n import lazy_gettext

    try:
        runner_app.control.discard_all()
        print db.session.query(Handin) \
            .filter(Handin.state.in_(['Pending', 'Running'])).count()
        db.session.query(Handin) \
            .filter(Handin.state.in_(['Pending', 'Running'])) \
            .update({
                'state': 'Rejected',
                'result': lazy_gettext('Submission discarded by admin.'),
                'partials': [],
                'score': 0.0,
            }, synchronize_session=False)
        db.session.commit()
        flash(_('All pending submissions are cleared.'), 'success')
    except Exception:
        app.logger.exception('Could not discard the pending submissions.')
        flash(_('Could not discard the pending submissions.'), 'danger')
    return redirect(url_for('.handins'))


@bp.route('/scores/')
@admin_required
def scores():
    """The admin page to list all homework assignments, each with a link
    to the homework score table.

    :route: /admin/scores/
    :method: GET
    :template: admin.scores.html
    """
    return render_template('admin.scores.html')


def _make_csv_report(q, display_headers, raw_headers, pagetitle, filename,
                     linker=(lambda colid, value: None)):
    def make_record(itm, hdr):
        if isinstance(itm, dict):
            return tuple(itm[h] for h in hdr)
        return tuple(getattr(itm, h) for h in hdr)

    # If a direct csv file is request
    if request.args.get('csvfile', None) == '1':
        io = StringIO()
        writer = csv.writer(io)
        writer.writerow(raw_headers)
        for itm in q:
            writer.writerow(make_record(itm, raw_headers))
        io.flush()
        io.seek(0, 0)   # important! we want send_file to read from the front
        return send_file(
            io,
            as_attachment=True,
            attachment_filename='%s.csv' % filename
        )

    # Otherwise show the page.
    return render_template(
        'admin.csvdata.html',
        headers=display_headers,
        items=[make_record(itm, raw_headers) for itm in q],
        pagetitle=pagetitle,
        linker=linker,
    )


@bp.route('/hwscores/<hwid>/')
@admin_required
def hwscores(hwid):
    """The admin page to view the student score table of a given homework.

    All users except the administrators will be listed on the table, even
    if he or she does not upload any submission.  Only the highest score
    of a user will be displayed.

    The view accepts a query string argument `csvfile`, and if `csvfile` is
    set to 1, a csv data file will be responded to the visitor instead of
    a html table page.

    :route: /admin/hwscores/<hwid>/
    :method: GET
    :template: admin.csvdata.html
    """
    def make_record(itm, hdr):
        return tuple([getattr(itm, h) for h in hdr])

    # Query about given homework
    hw = g.homeworks.get_by_uuid(hwid)
    if hw is None:
        raise NotFound(lazy_gettext('Requested homework not found.'))

    # Get max score for each user
    q = (db.session.query(Handin.user_id,
                          Handin.state,
                          User.name,
                          func.max(Handin.score * Handin.scale).label('score')).
         filter(Handin.hwid == hwid).
         join(User).
         group_by(Handin.user_id, Handin.state).
         having(Handin.state == 'Accepted'))

    # Show the report
    raw_headers = ['name', 'score']
    display_headers = [lazy_gettext('Username'), lazy_gettext('Score')]
    pagetitle = _('Scores for "%(hw)s"', hw=hw.info.name)
    filename = hw.info.name
    if isinstance(filename, unicode):
        filename = filename.encode('utf-8')

    # Pre-process the data
    # We need to display all users, even he does not submit anything!
    user_query = db.session.query(User.id, User.name)
    if not app.config['ADMIN_SCORE_IN_REPORT']:
        user_query = user_query.filter(func.not_(User.is_admin))
    users = sorted(
        (u.name, u.id) for u in user_query
    )
    user_scores = {}

    for rec in q:
        user_scores.setdefault(rec.user_id, 0.0)
        if user_scores[rec.user_id] < rec.score:
            user_scores[rec.user_id] = round_score(rec.score)

    # Build data in user name ASC
    csvdata = [
        {
            'name': u[0],
            'score': user_scores.get(u[1], '-')
        }
        for u in users
    ]

    # Link users to their submission page
    def LinkUser(idx, name):
        if idx == 0:
            return url_for('.handins_for_user', username=name)

    return _make_csv_report(
        csvdata,
        display_headers,
        raw_headers,
        pagetitle,
        filename,
        linker=LinkUser
    )


@bp.route('/get_longblob_patch_command/')
@admin_required
def get_longblob_patch_command():
    """As is mentioned in `models.py`, SQLAlchemy uses BLOB as the backend of
    PickleType in default, where the size of BLOB in MySQL is only 64K.  This
    will cause some Handin records be truncated, thus they cannot be fetched
    back into Railgun.

    We've now added patch to prevent this situation.  The existing broken
    records may be repaired simply by purging its detailed report data.
    This view just provides the SQL command to do so.
    """

    import sys
    import traceback

    def format_exception():
        return ''.join(traceback.format_exception(sys.exc_type, sys.exc_value,
                                                  sys.exc_traceback))

    err = []
    ids = []
    for o in db.session.query(Handin.id):
        idx = o.id
        try:
            db.session.query(Handin).filter(Handin.id == idx).one()
        except Exception:
            err.append('%s:\n%s' % (idx, format_exception()))
            ids.append(str(idx))

    recommend_sql = 'UPDATE handins SET partials = NULL WHERE id in (%s)' % (
        ','.join(ids))
    return make_response(
        recommend_sql + '\n' + '\n'.join(err),
        200,
        {'Content-Type': 'text/plain'}
    )


def make_charts_data(hw):
    """Make hwcharts data object."""
    ACCEPTED_AND_REJECTED = ('Accepted', 'Rejected')

    # Query about all the submission for this homework
    handins = (db.session.query(Handin).options(db.defer('partials')).
               join(User).
               filter(Handin.hwid == hw.uuid).
               filter(Handin.state.in_(ACCEPTED_AND_REJECTED)).
               filter(User.is_admin == 0))

    # The date histogram to count everyday submissions.
    def ListAdd(target, addition):
        for i, v in enumerate(addition):
            target[i] += v
        return target

    date_bucket = {}
    date_author_bucket = {}

    for obj in handins:
        dt = to_user_timezone(obj.get_ctime())
        key = dt.month, dt.day
        value = (1, int(obj.is_accepted()), int(not obj.is_accepted()))

        # We count the day freq
        if key in date_bucket:
            ListAdd(date_bucket[key], value)
        else:
            date_bucket[key] = list(value)

        # We count the day author freq
        if key not in date_author_bucket:
            date_author_bucket[key] = {obj.user.name}
        else:
            date_author_bucket[key].add(obj.user.name)

    date_author_bucket = {k: len(v) for k, v in date_author_bucket.iteritems()}

    # Cache the submission count of each user
    user_submit_bucket = {}

    for obj in handins:
        name = obj.user.name
        value = (1, int(obj.is_accepted()), int(not obj.is_accepted()))

        if name not in user_submit_bucket:
            user_submit_bucket[name] = list(value)
        else:
            ListAdd(user_submit_bucket[name], value)

    # Get the frequency of user submissions
    user_submit = {}
    for __, (total, __, __) in user_submit_bucket.iteritems():
        user_submit.setdefault(total, 0)
        user_submit[total] += 1

    # Get the score frequency of Accepted submissions
    user_finalscores = {}
    for obj in handins:
        name = obj.user.name
        score = obj.score or 0.0

        if name not in user_finalscores:
            user_finalscores[name] = score
        elif score > user_finalscores[name]:
            user_finalscores[name] = score

    final_score = group_histogram(
        user_finalscores.itervalues(),
        lambda v: round_score(v)
    )

    # Count the Accepted and Rejected submissions.
    acc_reject = group_histogram(
        handins,
        lambda d: d.state
    )

    # Count the number of the reasons for Rejected
    reject_brief = group_histogram(
        (h for h in handins if not h.is_accepted()),
        lambda d: unicode(d.result)
    )

    # Generate the JSON data
    json_obj = {
        'day_freq': sorted(date_bucket.items()),
        'day_author': sorted(date_author_bucket.items()),
        'acc_reject': [
            (k, acc_reject.get(k, 0))
            for k in ACCEPTED_AND_REJECTED
        ],
        'reject_brief': sorted(reject_brief.items()),
        'user_submit': sorted(user_submit.items()),
        'final_score': [
            (str(v[0]), v[1])
            for v in sorted(final_score.items())
        ],
    }
    return json_obj


@bp.route('/hwcharts/<hwid>/pack/')
@admin_required
def hwcharts_pack(hwid):
    """Download the packed homework chart data.

    :route: /admin/hwcharts/<hwid>/pack/
    :method: GET
    """
    hw = g.homeworks.get_by_uuid(hwid)
    if hw is None:
        raise NotFound(lazy_gettext('Requested homework not found.'))
    obj = make_charts_data(hw)

    # now we generate the different data text.
    resp = []
    delimeter = '-' * 79

    # first part, acc rate
    resp.append(_('Rate of Accepted'))
    resp.append(delimeter)
    for k, v in obj['acc_reject']:
        resp.append('%s\t%s' % (_(k), _(v)))
    resp.append('')

    # second part, the reason of rejected
    resp.append(_('Reasons for Rejected'))
    resp.append(delimeter)
    for k, v in obj['reject_brief']:
        resp.append('%s\t%s' % (k, v))
    resp.append('')

    # third part, every submission
    resp.append(_('Everyday Submission'))
    resp.append(delimeter)
    resp.append('%s\t%s\t%s' % (_('Date'), _('Accepted'), _('Rejected')))
    for k, v in obj['day_freq']:
        resp.append('%s/%s\t%s\t%s' % (k[0], k[1], v[1], v[2]))
    resp.append('')

    # fourth part, everyday submission author
    resp.append(_('Everyday Submitting Users'))
    resp.append(delimeter)
    resp.append('%s\t%s' % (_('Date'), _('User Count')))
    for k, v in obj['day_author']:
        resp.append('%s/%s\t%s' % (k[0], k[1], v))
    resp.append('')

    # fifth part, every author submission
    resp.append(_('Submissions Per User'))
    resp.append(delimeter)
    resp.append('%s\t%s' % (_('Submission'), _('User Count')))
    for k, v in obj['user_submit']:
        resp.append('%s\t%s' % (k, v))
    resp.append('')

    # sixth part, final score
    resp.append(_('Final Scores'))
    resp.append(delimeter)
    resp.append('%s\t%s' % (_('Score'), _('User Count')))
    for k, v in obj['final_score']:
        resp.append('%s\t%s' % (k, v))
    resp.append('')

    return make_response(
        '\n'.join(resp),
        200,
        {'Content-Type': 'text/plain; charset=utf-8'}
    )


@bp.route('/hwcharts/<hwid>/')
@admin_required
def hwcharts(hwid):
    """The admin page to view various of charts of a given homework.

    All users except the administrators will be considered to generate the
    charts.

    :route: /admin/hwcharts/<hwid>/
    :method: GET
    :template: admin.hwcharts.html
    """
    # Query about given homework
    hw = g.homeworks.get_by_uuid(hwid)
    if hw is None:
        raise NotFound(lazy_gettext('Requested homework not found.'))

    g.scripts.deps('chart.js')
    json_text = json.dumps(make_charts_data(hw))

    # Render the page
    return render_template('admin.hwcharts.html', chart_data=json_text,
                           hw=hw)


@bp.route('/vote/', methods=['GET', 'POST'])
@admin_required
def edit_vote():
    """Admin page to edit the vote.

    Railgun only supports one vote at this time.  The existing vote data
    will be purged.

    :route: /admin/vote/
    :method: GET, POST
    :template: admin.edit_vote.html
    """
    the_vote = Vote.query.filter().first()
    form = VoteJsonEditForm(obj=the_vote)

    # Import json source string from signup data
    from .utility import load_vote_signup, list_vote_signup, render_markdown
    if request.args.get('import') == '1':
        def MakeItem(itm):
            # determine the project name by project_id
            v = app.config['VOTE_PROJECT_NAMES']
            idx = itm['project_id']
            if idx < 0 or idx >= len(v):
                prjname = _('Unknown Project')
            else:
                prjname = v[idx]
            # determine the logo url
            if itm['logo_file']:
                logo_url = url_for('vote_static', filename=itm['logo_file'])
            else:
                logo_url = ''
            return {
                'title': u'%s by %s' % (prjname, itm['group_name']),
                'logo': logo_url,
                'desc': render_markdown(itm['description']),
            }

        def C(a, b):
            t = cmp(a['project_id'], b['project_id'])
            if t == 0:
                t = cmp(a['group_name'], b['group_name'])
            return t
        original_items = sorted(
            [load_vote_signup(fn) for fn in list_vote_signup()],
            cmp=C
        )
        items = [MakeItem(o) for o in original_items]
        json_obj = {
            'title': _('Vote for the Best Project'),
            'desc': _('Please vote for your favourite project! '
                      'You may vote for at least %(min)s project and '
                      'at most %(max)s project.', min=5, max=10),
            'items': items,
            'min_select': 5,
            'max_select': 10,
        }
        form.json_source.data = json.dumps(json_obj, indent=2)

    if form.validate_on_submit():
        try:
            # try to construct a new vote object
            obj = json.loads(form.json_source.data)
            obj['json_source'] = form.json_source.data
            new_vote = Vote()
            assign_values(new_vote, obj)

            # create the corresponding options
            for itm in obj['items']:
                new_option = VoteItem()
                assign_values(new_option, itm)
                new_vote.items.append(new_option)

            # now insert the vote into database, and delete the original one
            db.session.add(new_vote)
            if the_vote:
                db.session.delete(the_vote)
            db.session.commit()

            flash(_('Vote updated successfully.'), 'success')
            return redirect(url_for('.edit_vote'))
        except Exception:
            app.logger.exception('Error when updating vote.')
            flash(_('Internal server error, please try again.'), 'danger')

    return render_template('admin.edit_vote.html', form=form, vote=the_vote)


@bp.route('/vote/clear/')
@admin_required
def clear_vote():
    """Admin page to clear the vote.

    :route: /admin/vote/clear/
    """
    the_vote = Vote.query.filter().first()
    if the_vote is not None:
        db.session.delete(the_vote)
        try:
            db.session.commit()
            flash(_('Successfully purged the vote data.'), 'success')
        except Exception:
            app.logger.exception('Error when clearing the vote.')
            flash(_('Internal server error, please try again.'), 'danger')
    return redirect(url_for('.edit_vote'))


@bp.route('/vote/switch/<isopen>/')
@admin_required
def switch_vote(isopen):
    """Admin page to open or close the vote.

    :param isopen: "1" or "0" to indicate whether to open the vote.

    :route: /admin/switch/<isopen>/
    :method: GET
    """
    the_vote = Vote.query.filter().first()
    if not the_vote:
        raise NotFound()
    the_vote.is_open = (isopen == '1')
    db.session.commit()
    return redirect(url_for('.edit_vote'))


@bp.route('/vote/signup/')
@admin_required
def manage_vote_signup():
    """The page to manage vote signup data.

    :route: /admin/vote/signup/
    :method: GET
    :template: admin.manage_vote_signup.html
    """
    from .utility import list_vote_signup, load_vote_signup, render_markdown

    def MakeItem(itm, fn):
        # determine the project name by project_id
        v = app.config['VOTE_PROJECT_NAMES']
        idx = itm['project_id']
        if idx < 0 or idx >= len(v):
            prjname = _('Unknown Project')
        else:
            prjname = v[idx]
        itm['filename'] = fn
        itm['project_name'] = prjname
        itm['description'] = render_markdown(itm['description'])
        return itm

    def C(a, b):
        t = cmp(a['project_id'], b['project_id'])
        if t == 0:
            t = cmp(a['group_name'], b['group_name'])
        return t

    items = sorted(
        [MakeItem(load_vote_signup(fn), fn) for fn in list_vote_signup()],
        cmp=C
    )
    has_any_logo = sum(not not i['logo_file'] for i in items)

    return render_template(
        'admin.manage_vote_signup.html',
        items=items,
        has_any_logo=has_any_logo,
    )


@bp.route('/vote/signup/delete/<filename>/')
@admin_required
def delete_vote_signup(filename):
    """The page to delete vote signup data.

    :route: /admin/vote/signup/delete/<filename>/
    :method: GET
    """
    import os
    fpath = os.path.join(app.config['VOTE_SIGNUP_DATA_DIR'],
                         '%s.dat' % filename)
    if os.path.isfile(fpath):
        os.remove(fpath)
    return redirect(url_for('.manage_vote_signup'))


@bp.route('/vote/signup/edit/<filename>/', methods=['GET', 'POST'])
@admin_required
def edit_vote_signup(filename):
    """The page to edit vote signup data.

    :route: /admin/vote/signup/edit/<filename>/
    :method: GET
    """
    from .views import render_edit_vote_signup
    return render_edit_vote_signup(filename, 'admin.edit_vote_signup.html',
                                   '.manage_vote_signup')


# Register the blue print
app.register_blueprint(bp, url_prefix='/admin')

# Register navibars
#
# We must make sure that admin navigates appear after view nagivates, so
# just import views before navigates.add
from . import views
navigates.add(
    NaviItem(
        title=lazy_gettext('Manage'),
        url=None,
        identity='admin',
        adminpage=True,
        subitems=[
            NaviItem.make_view(title=lazy_gettext('Users'),
                               endpoint='admin.users'),
            NaviItem.make_view(title= lazy_gettext('Problems'),
                               endpoint='admin.problems'),
            NaviItem.make_view(title= lazy_gettext('Courses'),
                                     endpoint='admin.courses'),
            NaviItem.make_view(title=lazy_gettext('Submissions'),
                               endpoint='admin.handins'),
            NaviItem.make_view(title=lazy_gettext('Scores'),
                               endpoint='admin.scores'),
            NaviItem.make_view(title=lazy_gettext('Vote'),
                               endpoint='admin.edit_vote'),
            NaviItem.make_view(title=lazy_gettext('Vote Signup'),
                               endpoint='admin.manage_vote_signup'),
        ]
    )
)
