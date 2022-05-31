# -- coding: utf-8 --
'''https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'''
import requests
import re #正则表达式
import json
import csv
headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['area','curConfirm','confirmed','curConfirmRelative','crued','died'])
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
response = requests.get(url=url, headers=headers) #发送请求
#print(response) <200>访问成功
#print(response.text)
html_data = response.text
#解析数据
json_str = re.findall('"component":\[(.*)\],', html_data)[0]
print(json_str)
#print(json_str)
json_dict = json.loads(json_str)
caseList = json_dict['caseList']
caseOutsideList=json_dict["caseOutsideList"]
for case in caseList:
    area = case['area'] #省份
    curConfirm = case["curConfirm"]#确证
    confirmed = case["confirmed"]  # 累计确证
    curConfirmRelative = case["curConfirmRelative"]#当前确证
    crued = case["crued"]#累计治愈
    died = case["died"]#累计死亡
 #   print(area, curConfirm, curConfirmRelative, died, crued, confirmed)
    with open('data.csv',mode='a',encoding='utf-8',newline='')as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([area,curConfirm,confirmed,curConfirmRelative,crued,died])