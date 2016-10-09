#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from pyhost.saveLog import scoresData
from javahost.getScores import *
from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer, UnitTestScorer
import SafeRunner

scoresdata = scoresData(sys.argv[3]) #Don't change this!

if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromResult(getCodeStyleResult(), logs = scoresdata), 0.1), 
        # Note that the CoverageScorer takes 1.0 as total weight, but
        # uses stmt_weight=0.4, branch_weight=0.5 to control the score
        (CoverageScorer.FromResult(
            paras = getCoverageResult(['Succeed.java'], ['Succeed']),
            stmt_weight=0.6,
            branch_weight=0.3,
            logs = scoresdata,
        ), 1.0),
    ]
    SafeRunner.run(scorers)
    scoresdata.save()#Don't change this!
