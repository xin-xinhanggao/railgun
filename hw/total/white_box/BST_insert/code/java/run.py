#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from pyhost.scorer import CodeStyleScorer, CoverageScorer
import SafeRunner
from getScores import *

if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromResult(getCodeStyleResult()), 0.1), 
        # Note that the CoverageScorer takes 1.0 as total weight, but
        # uses stmt_weight=0.4, branch_weight=0.5 to control the score
        (CoverageScorer.FromResult(
            paras = getCoverageResult(['insert.java'], ['insert']),
            stmt_weight=0.4,
            branch_weight=0.5,
        ), 1.0),
    ]
    SafeRunner.run(scorers)
