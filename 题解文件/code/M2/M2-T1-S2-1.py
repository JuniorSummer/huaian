import pandas as pd
da = pd.read_csv('/root/travel/hotel/hotel.txt', sep='\t')

# 缺失数量统计

num = da['酒店类型'].isnull().sum()
# 删除指定列的缺失行

da = da.dropna(subset=['酒店类型'])
file_name ='/root/travel/hotel/hotel2_c1_'+ str(num)+'.csv'
da.to_csv(file_name, index=False, encoding='utf8')
