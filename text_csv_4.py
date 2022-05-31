# coding:utf-8
import xlrd
import os, json
from lxml import etree

xls = xlrd.open_workbook(os.getcwd() + '\student.xls')
sheet = xls.sheet_by_name("student")
Dict = {}
for row in range(sheet.nrows):
    Attr = sheet.row_values(row)  ##此处用法
    Dict[Attr[0]] = Attr[1:]  # 形成key-value对

# 如何操作xml
root = etree.Element('root')
child1 = etree.SubElement(root, "student")
comm = etree.Comment(u'学生信息表 "id":[名字，数学，名字，英文]')
child1.append(comm)
child1.text = unicode(json.dumps(Dict).decode('gbk'))

print
child1.text.decode('gbk')
tree = etree.ElementTree(root)
tree.write(os.getcwd() + '\student.xml')