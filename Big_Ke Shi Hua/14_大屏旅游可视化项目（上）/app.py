from random import randrange
from pyecharts import options as opts
from flask import Flask, render_template
from pyecharts.charts import Bar, Line, Pie, Radar, Funnel, Gauge, Map, Geo
from pyecharts.globals import ChartType, SymbolType

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/load_number')
def load_number():
    return [2558, 13960]


def bar_base() -> Bar:
    bar = (
        Bar(
            init_opts=opts.InitOpts(

            )
        )
        .add_xaxis(["长沙", "西安", "杭州", "上海", '重庆'])
        .add_yaxis("男性",
                    [randrange(0, 100) for _ in range(5)],
                    itemstyle_opts=opts.ItemStyleOpts(border_width=0, color='#2f89cf'),
                    category_gap='30%'
                    )
        .add_yaxis("女性",
                    [randrange(0, 100) for _ in range(5)],
                    itemstyle_opts=opts.ItemStyleOpts(border_width=0, color='#d47a82'),
                    category_gap='30%'
                    )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_left='center',
                pos_bottom='3%',
                border_width=0,
                inactive_color='#dddddd',
                textstyle_opts=opts.TextStyleOpts(color='#dddddd')
            ),
            title_opts=opts.TitleOpts(
                title='2023/12/05-热门城市旅游人次',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            )

        )
        .set_series_opts(
            label_opts=opts.LabelOpts(
                color='#dddddd',
                font_size=12,
                is_show=False
            )
        )

    )
    return bar


def line_base() -> Line:
    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月', '六月']
    man_data = [22, 32, 45, 25, 20, 47]
    woman_data = [20, 10, 62, 60, 40, 62]

    # 创建一个 Line 实例，并使用链式操作添加数据和设置属性
    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis("男性", man_data, xaxis_index=0, is_smooth=True,
                    itemstyle_opts=opts.ItemStyleOpts(border_width=0, color='#2f89cf'))
        .add_yaxis("女性", woman_data, xaxis_index=0, is_smooth=True,
                    itemstyle_opts=opts.ItemStyleOpts(border_width=0, color='#d47a82'))
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            title_opts=opts.TitleOpts(
                title='2023上半年男女旅游比例趋势',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_left='center',
                pos_bottom='3%',
                border_width=0,
                inactive_color='#dddddd',
                textstyle_opts=opts.TextStyleOpts(color='#dddddd')
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger='axis'
            )
        )
    )
    return line


def pie_base() -> Pie:
    # 定义数据和标签
    data = [120, 200, 150, 250, 300]
    labels = ["长沙", "重庆", "西安", "杭州", "上海"]

    # 创建一个 Line 实例，并使用链式操作添加数据和设置属性
    pie = (
        Pie(init_opts=opts.InitOpts(theme='light'))
        .add("", [list(z) for z in zip(labels, data)], rosetype='area')
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            title_opts=opts.TitleOpts(
                title='2023上半年热门城市人均消费占比',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_left='center',
                pos_bottom='3%',
                border_width=0,
                inactive_color='#dddddd',
                textstyle_opts=opts.TextStyleOpts(color='#dddddd')
            )
        )
        .set_series_opts(
            radius=["26%", "62%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False)
        )
    )
    return pie


def radar_base() -> Radar:
    # 创建 Radar 实例，并添加数据
    radar = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name='饮食', max_=10),
                opts.RadarIndicatorItem(name='风景', max_=10),
                opts.RadarIndicatorItem(name='文化', max_=10),
                opts.RadarIndicatorItem(name='空气质量', max_=10),
                opts.RadarIndicatorItem(name='热门度', max_=10),
            ],
            radius='50%',
            center=["50%", "55%"]
        )
        .add('长沙', [[8.5, 7.4, 9.3, 7.5, 9.8]], color='#ce6a73',
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#ce6a73"), )
        .add('武汉', [[3.9, 9.2, 2.5, 1.2, 8.5]], color='#bddbce',
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#bddbce"), )
        .add('上海', [[8.2, 3.5, 4.0, 9.5, 2.0]], color='#d0a983',
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#d0a983"), )
        .add('杭州', [[7.0, 1.8, 8.5, 6.5, 3.0]], color='#aba1f3',
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#aba1f3"), )
        .add('重庆', [[2.5, 8.8, 3.0, 8.5, 5.0]], color='#2e62ab',
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#2e62ab"), )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=6,
            symbol="circle"
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(color='#dddddd'),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#dddddd")
                )
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_left='center',
                pos_bottom='3%',
                border_width=0,
                inactive_color='#dddddd',
                textstyle_opts=opts.TextStyleOpts(color='#dddddd')
            ),
            title_opts=opts.TitleOpts(
                title='各大热门城市基本情况',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            ),
        )
    )
    return radar


def gauge_base(temperature: float) -> Gauge:
    # 创建仪表盘实例
    gauge = (
        Gauge()
        .add(
            series_name='长沙市',
            data_pair=[("", temperature)],
            radius='72%',
            min_=-10, max_=40,
            center=('50%', '60%'),
            detail_label_opts=opts.GaugeDetailOpts(is_show=False)
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title='当前热门城市平均温度',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            )
        )
        .set_series_opts(
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(width=30, color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]])
            ),
            detail_label_opts=opts.LabelOpts(formatter="{value}℃", font_size=20, color="#333"),
            label_opts=opts.LabelOpts(formatter="{value}", font_size=20, color="#333")
        )
    )

    return gauge


def funnel_base() -> Funnel:
    # 定义数据和标签
    labels = ['咨询', '报名', '缴费', '出游']
    values = [100, 60, 40, 35]

    # 创建漏斗图实例
    funnel = (
        Funnel(init_opts=opts.InitOpts(theme='light'))
        .add(
            series_name="流程",
            data_pair=list(zip(labels, values)),
            gap=5,
            tooltip_opts=opts.TooltipOpts(trigger='item', formatter='{a} <br/>{b} : {c}%'),
            label_opts=opts.LabelOpts(is_show=True, position='inside')
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_left='center',
                pos_bottom='3%',
                border_width=0,
                inactive_color='#dddddd',
                textstyle_opts=opts.TextStyleOpts(color='#dddddd')
            ),
            title_opts=opts.TitleOpts(
                title='2023年度参加旅游计划人数比例',
                pos_left='center',
                pos_top='10px',
                title_textstyle_opts=opts.TextStyleOpts(color='#dddddd', font_size=16)
            )
        )

    )

    return funnel


def map_base() -> Geo:
    geo = (
        Geo(

        )
        .add_schema(
            maptype='china',
            itemstyle_opts=opts.ItemStyleOpts(
                area_color='rgba(43, 196, 243, 0.42)',
                border_color='rgba(43, 196, 243, 1)',
            ),
            emphasis_itemstyle_opts=opts.ItemStyleOpts(
                area_color='rgba(43, 196, 243, 0.8)',
                border_color='rgba(43, 196, 243, 1)',
            ),
            emphasis_label_opts=opts.LabelOpts(
                color='yellow',
                font_size=12.5
            ),
            min_scale_limit=1,
            max_scale_limit=1,
        )
        .add(
            '',
            [('长沙市', 0), ('西安市', 0), ('乌鲁木齐市', 0), ('拉萨市', 0), ('吉林市', 0)],
            type_=ChartType.EFFECT_SCATTER,
            color='#ffffff',
            label_opts=opts.LabelOpts(
                color='#ffffff',
                position='right',
                margin=12,
                formatter='{b}',
                font_size=12.5,
                font_weight='bold',
                font_family='宋体'
            ),
        )
        .add(
            '',
            [('长沙市', '西安市'), ('长沙市', '拉萨市'), ('长沙市', '乌鲁木齐市'), ('长沙市', '吉林市')],
            type_=ChartType.LINES,
            color='#ffffff',
            linestyle_opts=opts.LineStyleOpts(
                curve=0.1
            ),
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW,
                color='#99ff99',
                symbol_size=14
            )
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .set_series_opts(

        )

    )
    return geo


@app.route("/mapChart")
def get_map_chart():
    china_map = map_base()
    return china_map.dump_options_with_quotes()


@app.route("/barChart")
def get_bar_chart():
    bar = bar_base()
    return bar.dump_options_with_quotes()


@app.route("/lineChart")
def get_line_chart():
    line = line_base()
    return line.dump_options_with_quotes()


@app.route("/pieChart")
def get_pie_chart():
    pie = pie_base()
    return pie.dump_options_with_quotes()


@app.route("/radarChart")
def get_radar_chart():
    radar = radar_base()
    return radar.dump_options_with_quotes()


@app.route("/funnelChart")
def get_funnel_chart():
    funnel = funnel_base()
    return funnel.dump_options_with_quotes()


@app.route("/gaugeChart")
def get_gauge_chart():
    gauge = gauge_base(25.6)
    return gauge.dump_options_with_quotes()


# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 确保使用非特权端口
