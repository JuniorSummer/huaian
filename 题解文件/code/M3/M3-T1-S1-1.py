import pandas as pd
da = pd.read_csv('/root/travel/hotel/district.csv')

#使用groupby方法根据'商圈'列对da DataFrame进行分组，并使用size方法计算每个商圈的酒店数量。
#然后，使用reset_index方法将结果转换为一个新的DataFrame，并给新列命名为'酒店数量'
hotel_sum = da.groupby('商圈').size().reset_index(name='酒店数量')

#按照酒店数量进行降序排序
top5_hotel = hotel_sum.sort_values('酒店数量',ascending=False).head(5)
print(top5_hotel)
top5_hotel.to_csv('/root/travel/hotel/hotel_sum.csv', index=None, encoding='UTF-8')
