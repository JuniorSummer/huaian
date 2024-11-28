import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 设置中文显示
plt.rcParams['axes.unicode_minus']=False # 解决负号'-'显示为方块的问题
#使用groupby方法根据'商圈'列对数据进行分组，并使用size方法计算每个商圈的酒店数量。
#使用reset_index方法将结果转换为DataFrame，并给新列命名为'酒店数量'。
#使用sort_values方法按照'酒店数量'列进行降序排序，并使用head(10)方法选择前10行。
da = pd.read_csv('/root/travel/hotel/district.csv', encoding='utf-8')
hotel_sum = da.groupby('商圈').size().reset_index(name='酒店数量')
top5_hotel = hotel_sum.sort_values('酒店数量',ascending=False).head(10)

#使用plt.figure设置图表的大小，宽度和高度，单位是英寸
#使用plt.bar创建柱状图，其中top5_hotel['商圈’]作为x轴数据，top5_hotel['酒店数量’]作为y轴数据。
#使用plt.title、plt.xlabel和plt.ylabel设置图表的标题和坐标轴标签。
#使用plt.show显示图表。
#使用plt.savefig将图表保存为'bar.png文件。
plt.figure(figsize=(20, 10))
plt.bar(top5_hotel['商圈'], top5_hotel['酒店数量'], color='skyblue')
plt.title('酒店数排名前十的商圈')
plt.xlabel('商圈')
plt.ylabel('酒店数量')
plt.show()
plt.savefig('/root/travel/hotel/bar.png')

