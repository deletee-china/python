import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line, EffectScatter
from pyecharts.charts import Page, Grid
from pyecharts.globals import ThemeType
# 读取数据
df = pd.read_csv('juanwang_comments.csv', encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('user_id')
df = df.dropna()
# 获取时间
df['time'] = [int(i.split(' ')[1].split(':')[0]) for i in df['comment_time']]
# 分组汇总
print(df['time'])
date_message = df.groupby(['time'])
date_com = date_message['time'].agg(['count'])
data = date_com.reset_index(inplace=False)
print(data)
# 绘制走势图
c = (Line(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add_xaxis(
    data['time']).add_yaxis("评论数目", data['count']).set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="24/评论条数"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    ))
df = pd.read_csv('../爬虫/dianzan.csv', encoding='utf-8-sig')
df['comment'] = [len(str(i)) for i in df['comment']]
co = (EffectScatter(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add_xaxis(df['comment']).add_yaxis(
    "点赞数", df['comment_dianzan']).set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="评论长度/点赞"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    ))
df = pd.read_csv('juanwang_comments.csv', encoding='utf-8-sig')
df = df.drop_duplicates('user_id')
df = df.dropna()
df['time'] = [int(i.split(' ')[0].replace('月',' ').replace('日',' ').split(' ')[1]) for i in df['comment_time']]
print(df['time'])
date_message = df.groupby(['time'])
date_com = date_message['time'].agg(['count'])
data = date_com.reset_index(inplace=False)
coo = (Line(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add_xaxis(
    data['time']).add_yaxis("评论数目", data['count']).set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="月份/评论数目"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    ))
page = (Page(layout=Page.SimplePageLayout).add(c).add(coo).add(co))
page.render("评论的可视化.html")
