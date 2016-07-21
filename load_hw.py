#!/usr/bin/python

from pymongo import MongoClient
from config import HOMEWORK_DIR
import os

problem_collection = MongoClient()["railgun"]["problem"]
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','reform_path'),"name":'reform_path',"ch_name":'格式化路径',"type":'black_box',"desc":'用于训练黑盒测试的题目，名字叫格式化路径'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','arith_api'),"name":'arith_api',"ch_name":'数学运算 API',"type":'black_box',"desc":'用于黑盒测试的题目，建立NetAPI来与server连接'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','black_box'),"name":'black_box',"ch_name":'黑色测试',"type":'black_box',"desc":'测试一下黑盒'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'white_box','white_box'),"name":'white_box',"ch_name":'白盒测试',"type":'white_box',"desc":'白盒测试的一道题'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'xunit','xunit'),"name":'xunit',"ch_name":'熟悉单元测试',"type":'xunit',"desc":'熟悉单元测试的一个样例，从这个样例中获得独特的单元测试体验'})
problem_collection.insert({"path":os.path.join(HOMEWORK_DIR,'black_box','test_black_box'),"name":'test_black_box',"ch_name":'测试用黑盒',"type":'black_box',"desc":'用来测试添加题目的机制可不可以用的黑盒测试'})