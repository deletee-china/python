from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


c = (
    Map(init_opts=opts.TitleOpts(theme=ThemeType.LIGHT))
    .add("商家A", [list(z) for z in zip(Faker.guangdong_city, Faker.values())], "中国")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guangdong.html")
)