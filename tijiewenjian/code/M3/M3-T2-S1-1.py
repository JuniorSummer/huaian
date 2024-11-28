import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simHei'] #显示中义，没置字体
plt.rcParams['axes.unicode_minus']=False #用米正常显示负号

#读取数据
da = pd.read_csv('/root/travel/hotel/standard.csv')
#对da数据框中的'情感倾向'列进行值计数，即统计每个不同情感倾向出现的次数
#结果存储在tendencies变量中，这是一个序列，索引为不同的情感倾向，值为对应的出现次数
tendencies = da['情感倾向'].value_counts()

#创建一个新的图形窗口，设置其大小为10x6英寸
#使用tendencies序列生成一个柱状图，柱子的颜色设置为天蓝色
#设置图表的标题为'情感倾向统计'
# 设置x轴的标签为'情感倾向'
#设置y轴的标签为'计数"
# 显示图表
plt.figure(figsize=(10, 6))
tendencies.plot(kind='bar', color='skyblue')
plt.title('情感倾向统计')
plt.xlabel('情感倾向')
plt.ylabel('计数')
plt.show()
plt.savefig('/root/travel/hotel/columnar.png')
