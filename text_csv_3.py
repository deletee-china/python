import  json
from collections import  OrderedDict #OrderedDict是字典的一个子模块他会根据字典输入的顺序对字典进行排序
import xlwt
with open('/Users/kein/Downloads/unemployment_male.txt',encoding='utf-8') as f:
    students_dict = json.load(f)#json.load()将已编码的json字符串解码成python对象,json.dumps()相反
    print(students_dict)

wb = xlwt.Workbook()  #创建一个工作簿
ws = wb.add_sheet('my sheets') #创建一个sheet

row = 0
for k,v in students_dict.items():
    ws.write(row,0,k)#xlwt模块 在表格中写入数据(行，列，值)
    ws.write(row,1,v)
    row +=1
wb.save('numbers.xls')  #保存