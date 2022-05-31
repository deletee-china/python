import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
df=pd.read_csv('data.csv',encoding='utf-8')
#print(df)
china_map=(
    Map()
    .add(
        '现有确诊',[list(i) for i in zip(df['area'].values.tolist(),df['curConfirm'].values.tolist())],'china'
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='各地区'),
        visualmap_opts=opts.VisualMapOpts(max_=100,is_inverse=True)
    )
    .add('累计死亡', [list(i) for i in zip(df['area'].values.tolist(), df['died'].values.tolist())], 'china')
)
china_map.render('demo.html')