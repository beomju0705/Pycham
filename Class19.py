import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import calendar

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

def create_sales_bar_chart(years, data):
    month = list(calendar.month_abbr)[1:]

    x = np.arange(len(month))
    bar_width = 0.25

    for i in range(len(years)):
        plt.bar(x + i * bar_width,
                data[i],
                tick_label=month,
                label = years[i],
                width = bar_width)
    plt.xlabel('월')
    plt.ylabel('판매량')
    plt.title('서초구 상점 물건 판매량')

    plt.legend()
    plt.show()

years = ['2022년', '2023년', '2024년']
data = data = [
    [50, 40, 30, 20, 60, 70, 80, 90, 100, 110, 120, 130],
    [60, 50, 40, 30, 80, 90, 100, 110, 120, 130, 140, 150],
    [50, 40, 30, 20, 60, 70, 80, 90, 100, 110, 120, 130]
]

create_sales_bar_chart(years, data)