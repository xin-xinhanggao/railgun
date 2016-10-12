#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from railgun.website.context import app
from pyhost.saveLog import scoresData
from pyhost.getScores import *
from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer, UnitTestScorer
import SafeRunner

scoresdata = scoresData(sys.argv[3]) #Don't change this!

if (__name__ == '__main__'):
    scorers = [
        (CodeStyleScorer.FromResult(getCodeStyleResult(), logs = scoresdata), 0.1), 
	(ObjSchemaScorer.FromResult(getSchemaResult(), logs = scoresdata), 0.9),
    ]
    SafeRunner.run(scorers) 
    scoresdata.save(app.config['ALLOW_LOG']) #Don't change this!

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
