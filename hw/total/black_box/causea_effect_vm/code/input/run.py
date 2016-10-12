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

@maker.class_("light off, 0.5 dollar's change,orange juice")
def test_1(obj):
    return (obj.a == 1) and (obj.b == 2) and (obj.c == 1)

@maker.class_("light off, 0.5 dollar's change,bear")
def test_2(obj):
    return (obj.a == 1) and (obj.b == 2) and (obj.c == 2)

@maker.class_("light off, no change,no drinks")
def test_3(obj):
    return (obj.a == 1) and (obj.b == 2) and (obj.c == 0)

@maker.class_("light off, no change,orange juice")
def test_4(obj):
    return (obj.a == 1) and (obj.b == 1) and (obj.c == 1)

@maker.class_("light off, no change,bear")
def test_5(obj):
    return (obj.a == 1) and (obj.b == 1) and (obj.c == 2)

@maker.class_("light off, no change,no drinks")
def test_6(obj):
    return (obj.a == 1) and (obj.b == 1) and (obj.c == 0)

@maker.class_("light off, no change,no drinks")
def test_7(obj):
    return (obj.a == 1) and (obj.b == 0) and (obj.c == 1)

@maker.class_("light off, no change,no drinks")
def test_8(obj):
    return (obj.a == 1) and (obj.b == 0) and (obj.c == 2)

@maker.class_("light on, return 1 dollar,no drinks")
def test_9(obj):
    return (obj.a == 0) and (obj.b == 2) and (obj.c == 1)

@maker.class_("light on, return 1 dollar,no drinks")
def test_10(obj):
    return (obj.a == 0) and (obj.b == 2) and (obj.c == 2)

@maker.class_("light on, no change,no drinks")
def test_11(obj):
    return (obj.a == 0) and (obj.b == 2) and (obj.c == 0)

@maker.class_("light on, no change,orange juice")
def test_12(obj):
    return (obj.a == 0) and (obj.b == 1) and (obj.c == 1)

@maker.class_("light on, no change,bear")
def test_13(obj):
    return (obj.a == 0) and (obj.b == 1) and (obj.c == 2)

@maker.class_("light on, no change,no drinks")
def test_14(obj):
    return (obj.a == 0) and (obj.b == 1) and (obj.c == 0)

@maker.class_("light on, no change,no drinks")
def test_15(obj):
    return (obj.a == 0) and (obj.b == 0) and (obj.c == 1)

@maker.class_("light on, no change,no drinks")
def test_16(obj):
    return (obj.a == 0) and (obj.b == 0) and (obj.c == 2)
# Run this scorer
SafeRunner.run(maker.get_scorers(weight=1.0))
scoresdata.save(app.config['ALLOW_LOG']) #Don't change this!
