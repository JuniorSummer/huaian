import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #解决负号'-'显示为方块的问题

# 读取数据
da = pd.read_csv('/root/travel/hotel/district.csv', encoding='utf-8')
#使用groupby方法按'酒店类型'对数据进行分组
#使用mean方法计算每个类型的酒店的评分平均值。
#使用reset_index方法将结果转换为DataFrame，并给新列命名为'平均评分'。
average = da.groupby('酒店类型')['评分'].mean().reset_index(name='平均评分')

#使用plt.plot函数绘制折线图，其中average['酒店类型']作为x轴数据，average['平均评分’]作为y轴数据。
#marker='o'表示在每个数据点上添加一个圆圈标记
plt.plot(average['酒店类型'], average['平均评分'], marker='o')

#添加标题和标签
plt.title('各类型酒店平均评分走势')
plt.xlabel('酒店类型')
plt.ylabel('平均评分')
plt.show()
plt.savefig('/root/travel/hotel/plot.png')
