#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os

from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer
from pyhost.objschema import RootSchema
import SafeRunner
from pyhost.saveLog import scoresData

scoresdata = scoresData(sys.argv[1]) #Don't change this!

# Define the schema of unit test objects
schema = RootSchema(os.environ['RAILGUN_ROOT'])

test_arith = schema.module('test_arith').require()
test_minmax = schema.module('test_minmax').require()

decrease_test_case = test_arith.class_('decreaseTestCase').require()
pow_test_case = test_arith.class_('PowTestCase').require()
get_max_test_case = test_minmax.class_('GetMaxTestCase').require()

decrease_test_case.method('test_positive_decrease_positive').require()
decrease_test_case.method('test_positive_decrease_negative').require()
decrease_test_case.method('test_negative_decrease_negative').require()

pow_test_case.method('test_positive_pow_positive').require()
pow_test_case.method('test_positive_pow_negative').require()
pow_test_case.method('test_negative_pow_positive_success').require()
pow_test_case.method('test_negative_pow_positive_failure').require()
pow_test_case.method('test_negative_pow_negative_success').require()
pow_test_case.method('test_negative_pow_negative_failure').require()

get_max_test_case.method('test_abc').require()
get_max_test_case.method('test_acb').require()
get_max_test_case.method('test_bac').require()
get_max_test_case.method('test_bca').require()
get_max_test_case.method('test_cab').require()
get_max_test_case.method('test_cba').require()


if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromHandinDir(ignore_files=['run.py'], logs = scoresdata), 0.1),
        (CoverageScorer.FromHandinDir(
            files_to_cover=['arith.py', 'minmax.py'],
            stmt_weight=0.5,
            branch_weight=0.5,
            logs = scoresdata,
        ), 0.2),
        (ObjSchemaScorer(schema, logs = scoresdata), 0.7),
    ]
    SafeRunner.run(scorers)
    scoresdata.save() #Don't change this!
