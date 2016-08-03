#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/website/api.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from railgun.common.csvdata import CsvSchema, CsvString
from config import User_Dir

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