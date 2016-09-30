#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer, UnitTestScorer
from pyhost.saveLog import scoresData
import SafeRunner
from getScores import *

scoresdata = scoresData(sys.argv[3]) #Don't change this!

if (__name__ == '__main__'):
    scorers = [
	(UnitTestScorer.FromResult(getUnitTestScore(), 15, logs = scoresdata), 0.4),
        (CodeStyleScorer.FromResult(getCodeStyleResult('arithTest.java'), logs = scoresdata), 0.1), 
	(ObjSchemaScorer.FromResult(getSchemaResult(), logs = scoresdata), 0.3),
	(CoverageScorer.FromResult(
            paras = getCoverageResult(['arith.java', 'minmax.java'], ['arith', 'minmax']),
            stmt_weight=1.0,
            branch_weight=0.0,
            logs = scoresdata
        ), 0.2),
    ]
    SafeRunner.run(scorers)
    scoresdata.save()


#if (__name__ == '__main__'):
#	score = getScore(cwd=sys.argv[1],
#		                env=eval(sys.argv[2]),
#		                close_fds=True)
#	scorers = [
#		(JavaScore(score), 1.0),
#	]
#	print type(scorers)
#	print type(JavaScore(score))
#	SafeRunner.run(scorers)
