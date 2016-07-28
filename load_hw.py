#!/usr/bin/python
#coding:utf-8
from pymongo import MongoClient
from config import HOMEWORK_DIR
import os

problem_collection = MongoClient()["railgun"]["problem"]
problem_collection.remove()
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','reform_path'),"name":'reform_path',"ch_name":'格式化路径',"type":'black_box',"desc":'用于训练黑盒测试的题目，名字叫格式化路径'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','arith_api'),"name":'arith_api',"ch_name":'数学运算 API',"type":'black_box',"desc":'用于黑盒测试的题目，建立NetAPI来与server连接'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','black_box'),"name":'black_box',"ch_name":'黑盒测试',"type":'black_box',"desc":'测试一下黑盒'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'white_box','white_box'),"name":'white_box',"ch_name":'白盒测试',"type":'white_box',"desc":'白盒测试的一道题'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'xunit','xunit'),"name":'xunit',"ch_name":'熟悉单元测试',"type":'xunit',"desc":'熟悉单元测试的一个样例，从这个样例中获得独特的单元测试体验'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','triangle_decision_table'),"name":'triangle_decision_table',"ch_name":'判定表三角形',"type":'black_box',"desc":'基于判定表的三角形测试用例'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','causea_effect_vm'),"name":'causea_effect_vm',"ch_name":'因果图售货机',"type":'black_box',"desc":'基于因果图的售货机测试用例'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'white_box','splay_tree_test'),"name":'splay_tree_test',"ch_name":'伸展树测试',"type":'white_box',"desc":'基于白盒测试的伸展树测试用例'})
