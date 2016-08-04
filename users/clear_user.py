#!/usr/bin/python
#coding:utf-8
from pymongo import MongoClient
import os

user_collection = MongoClient()["railgun"]["users"]
user_collection.remove()