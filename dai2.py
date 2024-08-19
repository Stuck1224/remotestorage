import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# Load data
file_path = "D:\\dai\\houseprice.xlsx"
data = pd.read_excel(file_path)

# Extract years and selected cities
years = data.columns[6:-2].tolist()
cities = ['安庆市', '蚌埠市', '亳州市', '池州市', '滁州市']
processed_data = pd.DataFrame(columns=['城市'] + years)

# Initialize line chart with theme and dimensions
line_chart = Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1200px", height="700px", bg_color="#1f1f1f"))
line_chart.add_xaxis(years)

# Define color palette for cities
color_palette = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"]

# Add data for each city to the chart
for idx, city in enumerate(cities):
    city_data = data.loc[data['市'] == city, years].values.flatten().tolist()
    city_data = [round(num, 2) for num in city_data]
    line_chart.add_yaxis(city, city_data, is_smooth=True,
                         linestyle_opts=opts.LineStyleOpts(width=3, color=color_palette[idx]),
                         areastyle_opts=opts.AreaStyleOpts(opacity=0.4, color=color_palette[idx]))

    # Append the city's data to the processed DataFrame
    new_row = pd.DataFrame([[city] + city_data], columns=processed_data.columns)
    processed_data = pd.concat([processed_data, new_row], ignore_index=True)

# Save processed data to CSV
processed_data.to_csv('processed_housing_data.csv', index=False, encoding='utf-8-sig')

# Set global options for the chart
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="逐年二手房房价变化趋势", subtitle="多个城市比较", pos_left="center", pos_top="95%",
                              title_textstyle_opts=opts.TextStyleOpts(color="#ffffff", font_size=18,
                                                                      font_weight="bold")),
    xaxis_opts=opts.AxisOpts(name="年份", axislabel_opts=opts.LabelOpts(color="#ffffff"),
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#ffffff")),
                             axistick_opts=opts.AxisTickOpts(is_show=True, length=8,
                                                             linestyle_opts=opts.LineStyleOpts(color="#ffffff"))),
    yaxis_opts=opts.AxisOpts(name="房价 (元/平方米)", axislabel_opts=opts.LabelOpts(color="#ffffff"),
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#ffffff")),
                             splitline_opts=opts.SplitLineOpts(is_show=True,
                                                               linestyle_opts=opts.LineStyleOpts(color="#555555"))),
    tooltip_opts=opts.TooltipOpts(trigger="axis", background_color="rgba(255, 255, 255, 0.8)", border_color="#aaaaaa",
                                  border_width=1, textstyle_opts=opts.TextStyleOpts(color="#000000")),
    legend_opts=opts.LegendOpts(pos_left="10%", textstyle_opts=opts.TextStyleOpts(color="#ffffff"),
                                background_color="rgba(0, 0, 0, 0.5)", border_color="#ffffff", border_width=1),
    toolbox_opts=opts.ToolboxOpts(is_show=True, orient="horizontal", pos_left="right"),
    visualmap_opts=opts.VisualMapOpts(is_show=False, min_=4000, max_=10000, range_color=["#6B5B95", "#FF6F61"])
)

# Render the chart to an HTML file
line_chart.render("房价变化趋势_多个城市_高级精美版.html")
