import requests
import  json
import pprint
import pandas as pd
url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=jQuery35104644799793502725_1651813642358&_=1651813642359'
response=requests.get(url,verify=False)
json_data=response.json()['data']
china_data=json_data['areatree'][0]['children']
data_set=[]
for i in china_data:
    data_dict={}
    data_dict['province']=i['name']
    data_dict['newConfirm']=i['total']['newConfirm']
    data_dict['dead']=i['total']['dead']
    data_dict['heal']=i['total']['heal']
    data_dict['deadRate']=i['total']['deadRate']
    data_dict['healRate']=i['total']['healRate']
    data_set.append(data_dict)
df=pd.DataFrame(data_set)
df.to_csv('data.csv')
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Pie,Map,Grid
df2=df.sort_values(by=['newConfirm'],ascending=False)[:9]
line = (
    Line()
    .add_xaxis(list(df['province'].values))
    .add_yaxis("治愈率", df['healRate'].values.tolist())
    .add_yaxis("死亡率", df['deadRate'].values.tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="死亡率与治愈率"),

    )
)
line.render_notebook()
bar = (
    Bar()
    .add_xaxis(list(df['province'].values)[:6])
    .add_yaxis("死亡", df['dead'].values.tolist()[:6])
    .add_yaxis("治愈", df['heal'].values.tolist()[:6])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各地区确诊人数与死亡人数情况"),
        datazoom_opts=[opts.DataZoomOpts()],
        )
)
bar.render_notebook()