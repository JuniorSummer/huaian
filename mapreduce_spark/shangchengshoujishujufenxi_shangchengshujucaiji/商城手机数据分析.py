import pandas as pd
import csv

#针对手机日志数据，对同一品牌手机进行相关分析，计算同一品牌:
# 手机总销售量；（同一品牌手机价格*销量）
# 总销售额；（同一品牌手机总销售额）
# 平均好评率。（同一品牌手机平均好评率=同一品牌手机总好评率/同一品牌手机总数，结果取整数）

data = pd.read_csv('mobile.txt', delimiter=',', encoding='utf-8')
# data = pd.read_csv('C:/Users/xiayu/Desktop/mobile.txt', delimiter=',', encoding='utf-8')

# 计算结果存储在字典中
brand_sales_info = {
    '品牌': [],
    '手机总销售量': [],
    '总销售额': [],
    '平均好评率': []
}

for brand, group in data.groupby('品牌'):
    brand_sales_info['品牌'].append(brand)
    # 计算同一品牌手机的总销售量
    brand_sales_info['手机总销售量'].append(group['销量'].sum())
    total_positive = 0
    total_sales = 0
    for index, row in group.iterrows():
        total_sales += (row['价格'] * row['销量'])
        total_positive += (row['好评率'] / 100 * row['销量'])
    # 计算同一品牌手机的平均好评率，用好评总数除销售额
    brand_sales_info['平均好评率'].append(round(total_positive / group['销量'].sum() * 100))
    # 计算同一品牌手机的总销售额，用每一种型号的手机销量*销售额再累加
    brand_sales_info['总销售额'].append(round(total_sales))

# 创建新的DataFrame以方便输出结果
result_df = pd.DataFrame(brand_sales_info)
# with open('part-r-00000.txt', 'w', encoding='utf-8') as f:
with open('part-r-00000', 'w', encoding='utf-8') as f:
    for index, row in result_df.iterrows():
        f.write(str(row['品牌']) + '\t' + str(row['手机总销售量']) + '\t' + str(row['总销售额']) + '\t' + str(row['平均好评率']))
        f.write('\n')