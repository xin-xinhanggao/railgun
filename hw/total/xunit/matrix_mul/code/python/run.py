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
        (CodeStyleScorer.FromHandinDir(ignore_files=['run.py']), 0.1),
        (CoverageScorer.FromHandinDir(
            files_to_cover=['operation.py'],
            stmt_weight=1.0,
            branch_weight=0.0,
        ), 0.2),
        (ObjSchemaScorer(schema), 0.7),
    ]
    SafeRunner.run(scorers)
