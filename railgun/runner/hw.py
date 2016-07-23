#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/runner/hw.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.
import os
from railgun.common.hw import HwSet
from . import runconfig

#: Load the homeworks under ``config.HOMEWORK_DIR`` at the startup of runner
#: queue.

homeworks = HwSet(runconfig.HOMEWORK_DIR,[''])
for p_path in os.listdir(runconfig.COURSE_HOMEWORK_DIR):
    r_path = os.path.join(runconfig.COURSE_HOMEWORK_DIR,p_path)
    if os.path.isdir(r_path):
        homeworks.add_hw(r_path)

#for homework in homeworks.items:
#    print homework.uuid