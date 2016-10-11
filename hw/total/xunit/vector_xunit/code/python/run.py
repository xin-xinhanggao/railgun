#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os

from railgun.website.context import app
from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer
from pyhost.objschema import RootSchema
import SafeRunner
from pyhost.saveLog import scoresData

scoresdata = scoresData(sys.argv[1]) #Don't change this!

# Define the schema of unit test objects
schema = RootSchema(os.environ['RAILGUN_ROOT'])

test_operation = schema.module('test_operation').require()
test_get_vertical = schema.module('test_get_vertical').require()

cross_test_case = test_operation.class_('crossTestCase').require()
dot_test_case = test_operation.class_('dotTestCase').require()
verticalTestCase = test_get_vertical.class_('verticalTestCase').require()

cross_test_case.method('test_zero_cross_zero').require()
cross_test_case.method('test_zero_cross_normal').require()
cross_test_case.method('test_p1_cross_p2').require()
cross_test_case.method('test_n1_cross_n2').require()

dot_test_case.method('test_zero_dot_zero').require()
dot_test_case.method('test_zero_dot_n1').require()
dot_test_case.method('test_v1_dot_v2').require()
dot_test_case.method('test_n1_dot_n2').require()

verticalTestCase.method('test_z_z').require()
verticalTestCase.method('test_z_n').require()
verticalTestCase.method('test_p_p').require()
verticalTestCase.method('test_n_n').require()


if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromHandinDir(ignore_files=['run.py','get_vertical.py','operation.py','vector.py'], logs = scoresdata), 0.1),
        (CoverageScorer.FromHandinDir(
            files_to_cover=['get_vertical.py', 'operation.py'],
            stmt_weight=1.0,
            branch_weight=0.0,
            logs = scoresdata,
        ), 0.2),
        (ObjSchemaScorer(schema, logs = scoresdata), 0.7),
    ]
    SafeRunner.run(scorers)
    scoresdata.save(app.config['ALLOW_LOG']) #Don't change this!
