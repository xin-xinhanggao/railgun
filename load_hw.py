#!/usr/bin/python

from pymongo import MongoClient
from config import HOMEWORK_DIR
from config import HOMEWORK_TYPE_SET
import os

def main():
    collection = MongoClient()["railgun"]["course"]
    collection.insert({"path":'/Users/apple/railgun/hw/course/',"problem_list":"reform_path@arith_api@black_box","name":'2016'})
    """
    problem = collection.find_one({"xxx":"s"})
    problem_dict = problem['name']
    print type(problem_dict)
    print problem_dict
    try:
        collection.insert({"name": {"abcs":"d"}, "path":"b","xxx":"s","sdasd":"xxx"})
    except:
        print "insert error"
    """
if __name__ == '__main__':
    main()
    