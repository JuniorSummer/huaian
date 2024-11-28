import pandas as pd
df = pd.read_csv('/root/travel/hotel/hotels.txt', sep = '\t')

# 缺失数量
num = df['最热评价'].isnull().sum()

# 删除指定列的缺失行
df = df.dropna(subset=['最热评价'])
file_name ='/root/travel/hotel/hotel_comment.csv'
df.to_csv(file_name, index=False, encoding='utf8')
