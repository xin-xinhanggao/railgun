#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/chkpath/code/python/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import sys

from pyhost.scorer import JavaScore
import SafeRunner
import subprocess

def getScore(**kwargs):
	p = subprocess.Popen("sh mv.sh && sh run.sh && java Test/unitTest", shell = True,
						stdout = subprocess.PIPE,
						stderr = subprocess.PIPE,
						**kwargs)
	ph_out, ph_err = p.communicate()
	#return ph_out
	print "ph_out : " + str(ph_out)
	return 100



if (__name__ == '__main__'):
	score = getScore(cwd=sys.argv[1],
		                env=eval(sys.argv[2]),
		                close_fds=True)
	scorers = [
		(JavaScore(score), 1.0),
	]
	print type(scorers)
	print type(JavaScore(score))
	SafeRunner.run(scorers)
