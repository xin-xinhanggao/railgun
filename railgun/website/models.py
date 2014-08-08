#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/website/models.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contributors:
#   public@korepwx.com   <public@korepwx.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from datetime import datetime

from babel.dates import UTC
from flask.ext.babel import gettext
from werkzeug.security import generate_password_hash, check_password_hash

from .context import db

# define the states of all handins
_ = lambda s: s
HANDIN_STATES = (_('Pending'), _('Running'), _('Error'), _('Accepted'))


class User(db.Model):
    __tablename__ = 'users'

    # User passport
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(50))

    # Relationship between User and Handin records
    handins = db.relationship('Handin')

    # Basic model object interfaces
    def __repr__(self):
        return "<User(%s)>" % (self.name)

    # Password should be stored as salted hash text. These methods provide
    # updating and validation of the password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Handin(db.Model):
    __tablename__ = 'handins'

    # We use uuid to seek particular Handin, but we maintain an integral id.
    # This is because some databases lack a full support for UUIDs.
    id = db.Column(db.Integer, db.Sequence('handin_id_seq'), primary_key=True)
    uuid = db.Column(db.String(32), unique=True)

    # We store datetime in UTC anyway. But we do not store the timestamp
    # in database.
    ctime = db.Column(db.DateTime, default=datetime.utcnow())

    # A handin is associated with certain homework and programming language
    hwid = db.Column(db.String(32), index=True)
    lang = db.Column(db.String(32))

    # There should be states of handins:
    state = db.Column(db.Enum(*HANDIN_STATES), default='Pending', index=True)

    # The result of given handin should include score, scale, run_time,
    # brief report and detailed report
    #
    # the brief report and detailed report should be lazy_gettext instance,
    # so we should use db.PickleType to store these reports
    score = db.Column(db.Float)
    scale = db.Column(db.Float)
    run_time = db.Column(db.Float)
    brief_report = db.Column(db.PickleType)
    detail_report = db.Column(db.PickleType)

    # db.ForeignKey to the User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Basic model object interface
    def __repr__(self):
        return '<Handin(%s)>' % self.uuid

    def get_ctime(self):
        """Get the ctime with UTC tzinfo"""
        return self.ctime.replace(tzinfo=UTC)

    def set_ctime(self, ctime):
        """Set UTC `ctime` with no tzinfo"""
        self.ctime = ctime.replace(tzinfo=None)

    def get_state(self):
        """Get translated state name"""
        return gettext(self.state)

db.create_all()
