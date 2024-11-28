import pandas as pd
da = pd.read_csv('/root/travel/hotel/district.csv')

#使用groupby方法根据'商圈'列对da DataFrame进行分组，并使用size方法计算每个商圈的酒店数量。
#然后，使用reset_index方法将结果转换为一个新的DataFrame，并给新列命名为'酒店数量'。
area_counts = da.groupby('商圈').size().reset_index(name='酒店数量')

# 按照酒店数量进行降序排序，并选择排名前三的商圈。然后，使用tolist方法将'商圈'列的值转换为一个列表。
top_three_areas = area_counts.sort_values('酒店数量',ascending=False).head(3)['商圈'].tolist()

#使用isin方法筛选出da DataFrame中'商圈’列值在前三个商圈列表top_three_areas中的记录，并将筛选后的数据存储在filtered_data中。
filtered_data = da[da['商圈'].isin(top_three_areas)]

#最后，我们对筛选后的数据按照商圈和酒店类型进行分组统计,并使用size方法计算每个组(即每个商圈和酒店类型的组合)的酒店数量。
#然后，使用reset_index方法将结果转换为一个新的DataFrame，并给新列命名为'数量'
hotel_type_counts = filtered_data.groupby(['商圈','酒店类型']).size().reset_index(name='数量')
hotel_type_counts.to_csv('/root/travel/hotel/types.csv',index=None,encoding='UTF-8')
