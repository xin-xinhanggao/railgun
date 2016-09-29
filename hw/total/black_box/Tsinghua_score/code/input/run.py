#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/black_box/code/input/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from railgun.common.csvdata import CsvSchema, CsvFloat
from pyhost.scorer import BlackBoxScorerMaker
import SafeRunner


class Score(CsvSchema):
    a = CsvInteger()

maker = BlackBoxScorerMaker(
    schema=Score,
    csvdata=open('data.csv', 'rb'),
    input_class_weight=0.9,
    boundary_value_weight=0.1,
)

@maker.class_('level A')
def levelA1(obj):
    return (obj.a >= 95 && obj.a < 100)

@maker.class_('level A-')
def levelA2(obj):
    return (obj.a >= 90 && obj.a < 95)

@maker.class_('level B+')
def levelB1(obj):
    return (obj.a >= 85 && obj.a < 90)

@maker.class_('level B')
def levelB2(obj):
    return (obj.a >= 80 && obj.a < 85)

@maker.class_('level B-')
def levelB3(obj):
    return (obj.a >= 77 && obj.a < 80)

@maker.class_('level C+')
def levelC1(obj):
    return (obj.a >= 73 && obj.a < 77)

@maker.class_('level C')
def levelC2(obj):
    return (obj.a >= 70 && obj.a < 73)

@maker.class_('level C-')
def levelC3(obj):
    return (obj.a >= 67 && obj.a < 70)

@maker.class_('level D+')
def levelD1(obj):
    return (obj.a >= 63 && obj.a < 67)

@maker.class_('level D')
def levelD2(obj):
    return (obj.a >= 60 && obj.a < 63)

@maker.class_('level F')
def levelF(obj):
    return (obj.a >= 0 && obj.a < 60)


@maker.class_('overflow')
def levelO(obj):
    return (obj.a > 100 && obj.a < 0)

@maker.boundary('level A+')
def leavelA22(obj):
    return obj.a == 100

# Run this scorer
SafeRunner.run(maker.get_scorers(weight=1.0))
