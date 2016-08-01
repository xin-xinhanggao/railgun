#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from pyhost.scorer import JavaScore
from pyhost.scorer import CodeStyleScorer, ObjSchemaScorer, CoverageScorer, UnitTestScorer
import SafeRunner
import subprocess
import javacoverage

def getScore(**kwargs):
	p = subprocess.Popen("sh mv.sh && sh run.sh && java Test/unitTest", shell = True,
						stdout = subprocess.PIPE,
						stderr = subprocess.PIPE,
						**kwargs)
	ph_out, ph_err = p.communicate()
	#return ph_out
	print "ph_out : " + str(ph_out)
	return 100

def getCodeStyleResult(JavaFile):
	return open('codestyle', 'r').read()

def getSchemaResult():
	p = subprocess.Popen('java testSchema', shell=True,
		         stdout=subprocess.PIPE,
		         stderr=subprocess.PIPE)

	ph_ret = p.wait()
	ph_out, ph_err = p.communicate()
	return ph_out

def getUnitTestScore(filename):
	p = subprocess.Popen('java %s'%(filename), shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

	ph_ret = p.wait()
	ph_out, ph_err = p.communicate()
	print ph_out
	return ph_out

def getCoverageResult(filename, classname):
	result = []

	for i in xrange(len(filename)):
		result.append(javacoverage.singleFile(filename[i], classname[i]))
	return result

if (__name__ == '__main__'):
    scorers = [
	(UnitTestScorer.FromResult(getUnitTestScore('unitTest'), 15), 0.4),
        (CodeStyleScorer.FromResult(getCodeStyleResult('arithTest.java')), 0.1), 
	(ObjSchemaScorer.FromResult(getSchemaResult()), 0.3),
	(CoverageScorer.FromResult(
            paras = getCoverageResult(['arith.java'], ['arith']),
            stmt_weight=1.0,
            branch_weight=0.0,
        ), 0.2),
    ]
    SafeRunner.run(scorers)


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
