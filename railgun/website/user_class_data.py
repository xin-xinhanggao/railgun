#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/website/api.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from railgun.common.csvdata import CsvSchema, CsvString
from config import User_Dir
from .context import app, db
from .models import User, Handin, FinalScore


class User_Schema(CsvSchema):

    stdno = CsvString(name='student-number')
    course = CsvString()

user_dic = {}
with open(User_Dir, 'rb') as f:
    for obj in CsvSchema.LoadCSV(User_Schema, f):
        user_dic.update({obj.stdno:obj.course})

def update():
    global user_dic
    user_dic = {}
    with open(User_Dir, 'rb') as f:
        for obj in CsvSchema.LoadCSV(User_Schema, f):
            user_dic.update({obj.stdno:obj.course})
    users = User.query.filter()
    for user in users:
        if user.provider == "tsinghua":
            course = user_dic.get(user.name,None)
            if course == None:
                # the user need to be deleted form mongo and sql
                # Delete all top scores of this user
                FinalScore.query.filter(FinalScore.user_id == user.id).delete()
                # Delete all submissions of this user
                Handin.query.filter(Handin.user_id == user.id).delete()
                # Delete this user
                User.query.filter(User.id == user.id).delete()
                # commit the changes
                db.session.commit()
                if app.config['USERS_COLLECTION'].count({"_id":user.name}) > 0:
                    app.config['USERS_COLLECTION'].remove({"_id":user.name})
