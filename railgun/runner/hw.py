#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/runner/hw.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.
import os
from . import runconfig
from railgun.common.hw import HwSet

#: Load the homeworks under ``config.HOMEWORK_DIR`` at the startup of runner
#: queue.

homeworks = HwSet(runconfig.HOMEWORK_DIR,[''])
if not os.path.isdir(runconfig.COURSE_HOMEWORK_DIR):
    os.mkdir(runconfig.COURSE_HOMEWORK_DIR)

homeworks.course_init(runconfig.HOMEWORK_DIR)

def update_homework(uuid,homework_path):
    global homeworks
    homeworks.update_homework(uuid,homework_path)

def add_homework(homework_path):
    global homeworks
    homeworks.add_homework(homework_path)

def delete_homework(uuid):
    global homeworks
    homeworks.delete_homework(uuid)
