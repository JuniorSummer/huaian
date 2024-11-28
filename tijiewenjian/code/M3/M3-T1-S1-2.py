import pandas as pd
da = pd.read_csv('/root/travel/hotel/district.csv')

# 从da DataFrame中提取名为'起价'的列，并将其转换为列表。然后，遍历这个列表，移除每个元素中的'￥’和'起'字符，并将剩余部分转换为整数。
# 最后，将转换后的整数列表转换为一个pandas Series对象。
a = da['起价']
a = list(a)
a = [int(a.replace("¥","").replace("起","")) for a in a]
a = pd.Series(a)

# 使用新的Series a 创建一个新的DataFrame d，其中列名为'最低价'
# 然后，使用pd.concat将da和d沿着列方向(axis=1)合并，得到一个新的DataFrame shu.
a.head()
d = pd.DataFrame({'最低价': a})
shu = pd.concat([da, d], axis=1)
shu.head()

#使用groupby方法根据'商圈'列对shu DataFrame进行分组，并使用mean方法计算每个商圈的'最低价'列的平均值。
#然后，使用reset_index方法将结果转换为一个新的DataFrame，并给新列命名为'平均最低价'。
area_counts = shu.groupby('商圈')['最低价'].mean().reset_index(name='平均最低价')

#对area_counts DataFrame按照'平均最低价'列进行排序，并使用head(5)方法选择前五行(即平均最低价最低的五个商圈)
top_five = area_counts.sort_values('平均最低价').head(5)
print(top_five)
top_five.to_csv('/root/travel/hotel/price_mean.csv',index=None,encoding='UTF-8')
