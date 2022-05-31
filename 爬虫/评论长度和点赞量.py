import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import EffectScatter
df = pd.read_csv('dianzan.csv', encoding='utf-8-sig')
df['comment']=[len(str(i))for i in df['comment']]
c=(
   EffectScatter()
    .add_xaxis(df['comment'])
    .add_yaxis("点赞数",df['comment_dianzan'])
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="点赞和评论长度"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
    .render("评论长度和点按数的可视化.html")
)
