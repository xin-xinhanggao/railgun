#coding: utf-8
from csvdata import CsvSchema
from csvdata import CsvInteger
from csvdata import CsvString
from csvdata import CsvFloat
from csvdata import CsvBoolean


class MyObjectSchema(CsvSchema):
    
    stdno = CsvString(name='a')
    name = CsvString(name = 'b')
    department = CsvString(name='c')
    _class = CsvString(name='d')
    _type = CsvString(name = 'e')
    _email = CsvString(name = 'f')
    _phone = CsvString(name = 'g')

s = 'CST软件工程'
w = open('users.csv', 'w')
w.write('student-number,course\n')
with open('new.csv', 'rb') as f:
    for obj in CsvSchema.LoadCSV(MyObjectSchema, f):
        w.write(str(obj.stdno) + "," )
        w.write(s)
        w.write("\n")