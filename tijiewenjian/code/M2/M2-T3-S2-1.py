import pandas as pd
# 使用pandas库的read_csv函数读取名为'hotel.txt"的文件，并指定分隔符为制表符\t。读取后的数据存储在da这个DataFrame中。
da = pd.read_csv('/root/travel/hotel/hotel.txt', sep = '\t')

#从da中提取'位置信息'这一列，并替换其中的"·"为逗号,。这步操作是为了统一数据格式，方便后续的分列操作
localtion = da['位置信息']
localtion = [localtion.replace("·",",")for localtion in localtion]

# 将处理后的localtion列表转换为一个新的DataFrame，并使用逗号,作为分隔符进行分列。分列后的数据有两列，分别命名为'商圈'和'景点'
delimiter =','
df = pd.DataFrame(localtion, columns=['Column1'])['Column1'].str.split(delimiter, expand=True)
df = df.rename(columns={0:'商圈', 1:'景点'})
#使用pd.concat函数将原始的da DataFrame和分列后的df DataFrame按列合并，合并后的数据存储在sss中
sss = pd.concat([da, df], axis=1)

#再次将sss转换为DataFrame
shu=pd.DataFrame(sss)
print(sss.head(10))

# index=None:不保存索引
wenben=shu.to_csv('/root/travel/hotel/district.csv', index=None, encoding='UTF-8')
