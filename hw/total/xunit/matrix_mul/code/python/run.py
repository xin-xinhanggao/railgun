#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from railgun.website.context import app
from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer
from pyhost.objschema import RootSchema
import SafeRunner
from pyhost.saveLog import scoresData

scoresdata = scoresData(sys.argv[1]) #Don't change this!

# Define the schema of unit test objects
schema = RootSchema(os.environ['RAILGUN_ROOT'])

test_operation = schema.module('test_operation').require()

check_test_case = test_operation.class_('CheckTestCase').require()
mul_test_case = test_operation.class_('MulTestCase').require()

check_test_case.method('test_empty').require()
check_test_case.method('test_column_different').require()
check_test_case.method('test_item_type').require()
check_test_case.method('test_legal').require()

mul_test_case.method('test_legal_mul_illegal').require()
mul_test_case.method('test_illegal_mul_legal').require()
mul_test_case.method('test_illegal_mul_illegal').require()
mul_test_case.method('test_scale_error').require()
mul_test_case.method('test_legal').require()

if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromHandinDir(ignore_files=['run.py', 'operation.py'], logs = scoresdata), 0.1),
        (ObjSchemaScorer(schema, logs = scoresdata), 0.9),
    ]
    SafeRunner.run(scorers)
    scoresdata.save(app.config['ALLOW_LOG']) #Don't change this!
