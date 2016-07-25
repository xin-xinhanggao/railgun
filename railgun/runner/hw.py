#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/runner/hw.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.
import os
from . import runconfig
from railgun.common.hw import HwSet
from railgun.common.hw import Homework
from railgun.website.hw import HwProxy

#: Load the homeworks under ``config.HOMEWORK_DIR`` at the startup of runner
#: queue.

homeworks = HwSet(runconfig.HOMEWORK_DIR,[''])
if not os.path.isdir(runconfig.COURSE_HOMEWORK_DIR):
    os.mkdir(runconfig.COURSE_HOMEWORK_DIR)

for p_path in os.listdir(runconfig.COURSE_HOMEWORK_DIR):
    r_path = os.path.join(runconfig.COURSE_HOMEWORK_DIR,p_path)
    if os.path.isdir(r_path):
        homeworks.add_hw(r_path)

def get_homework_index(uuid):
    global homeworks
    index = 0
    for homework in homeworks.items:
        if homework.uuid == uuid:
            return index
        index = index + 1
    return len(homeworks.items)

def update_homework(uuid,homework_path):
    global homeworks
    homework_index = get_homework_index(uuid)
    if homework_index == len(homeworks.items):
        print "update error"
        return
    if(os.path.isdir(homework_path) and os.path.isfile(os.path.join(homework_path,'hw.xml'))):
        homework = Homework.load(homework_path)
        homeworks.items[homework_index] = homework

def add_homework(homework_path):
    global homeworks
    if(os.path.isdir(homework_path) and os.path.isfile(os.path.join(homework_path,'hw.xml'))):
        homework = Homework.load(homework_path)
        homeworks.items.append(homework)

def delete_homework(uuid):
    global homeworks
    homework_index = get_homework_index(uuid)
    if homework_index != len(homeworks.items):
        del homeworks.items[homework_index]
    else:
        print "delete error"