#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: hw/black_box/code/input/run.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from railgun.website.context import app
from railgun.common.csvdata import CsvSchema, CsvFloat
from pyhost.scorer import BlackBoxScorerMaker
import SafeRunner
from pyhost.saveLog import scoresData

scoresdata = scoresData(sys.argv[1]) #Don't change this!

# Initialize the scorer with CSV schema and data
class TriangleArgs(CsvSchema):
    """Data schema for `triangle_type` method arguments."""

    a = CsvFloat()
    b = CsvFloat()
    c = CsvFloat()

maker = BlackBoxScorerMaker(
    schema=TriangleArgs,
    csvdata=open('data.csv', 'rb'),
    input_class_weight=1.0,
    boundary_value_weight=0.0,
    logs=scoresdata
)


# Add input class rules
@maker.class_('illegal triangle a >= b + c')
def illegal_triangle_1(obj):
    return not(obj.a < obj.b + obj.c)

@maker.class_('illegal triangle b >= a + c')
def illegal_triangle_2(obj):
    return (obj.a < obj.b + obj.c) and (not(obj.b < obj.a + obj.c))

@maker.class_('illegal triangle c >= a + b')
def illegal_triangle_3(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and (not(obj.c < obj.a + obj.b))

@maker.class_('regular triangle')
def regular_triangle(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and(obj.c < obj.a + obj.b) and (obj.a == obj.b) and (obj.a == obj.c) and (obj.b == obj.c)

@maker.class_('isosceles triangle a == b')
def isosceles_triangle_1(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and(obj.c < obj.a + obj.b) and (obj.a == obj.b) and (not(obj.a == obj.c)) and (not(obj.b == obj.c))

@maker.class_('isosceles triangle a == c')
def isosceles_triangle_2(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and(obj.c < obj.a + obj.b) and (not(obj.a == obj.b)) and (obj.a == obj.c) and (not(obj.b == obj.c))

@maker.class_('isosceles triangle b == c')
def isosceles_triangle_3(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and(obj.c < obj.a + obj.b) and (not(obj.a == obj.b)) and (not(obj.a == obj.c)) and (obj.b == obj.c)

@maker.class_('normal triangle')
def normal_triangle(obj):
    return (obj.a < obj.b + obj.c) and (obj.b < obj.a + obj.c) and(obj.c < obj.a + obj.b) and (not(obj.a == obj.b)) and (not(obj.a == obj.c)) and (not(obj.b == obj.c))

# Run this scorer
SafeRunner.run(maker.get_scorers(weight=1.0))
scoresdata.save(app.config['ALLOW_LOG']) #Don't change this!
