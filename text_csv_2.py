import  json
from collections import  OrderedDict #OrderedDict是字典的一个子模块他会根据字典输入的顺序对字典进行排序
import xlwt
with open('/Users/kein/Downloads/unemployment_male.txt',encoding='utf-8') as f:
    students_dict = json.load(f)#json.load()将已编码的json字符串解码成python对象,json.dumps()相反
wb = xlwt.Workbook()  #创建一个工作簿
ws = wb.add_sheet('my sheets') #创建一个sheet
rows=0
for k in students_dict:#.iterms遍历字典用
    row=0
    for b in k :
        ws.write(rows,row,b)
        row+=1#xlwt模块 在表格中写入数据(行，列，值)
    rows+=1

wb.save('numbers.xls')  #保存