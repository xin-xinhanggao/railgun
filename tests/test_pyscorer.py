#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: tests/pyscorer.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contributors:
#   public@korepwx.com   <public@korepwx.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import unittest
from pyhost.scorer import UnitTestScorer


class UnitTestScorerTestCase(unittest.TestCase):

    class MyTest(unittest.TestCase):

        def test_success(self):
            self.assertEqual(1, 1)

        def test_failure(self):
            self.assertEqual(1, 2)

        def test_error(self):
            raise ValueError('This is test error.')

        @unittest.skip('Demonstration skipping')
        def test_skip(self):
            pass

        @unittest.expectedFailure
        def test_expectedFailure(self):
            self.assertEqual(1, 2)

        @unittest.expectedFailure
        def test_unexpectedSuccess(self):
            self.assertEqual(1, 1)

    def test_scorer(self):
        scorer = UnitTestScorer(
            unittest.TestLoader().loadTestsFromTestCase(
                UnitTestScorerTestCase.MyTest
            )
        )
        scorer.run()
        # check the result patterns
        self.assertAlmostEqual(4*100.0/6, scorer.score)
