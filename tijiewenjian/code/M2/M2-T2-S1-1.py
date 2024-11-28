#从当前行中获取“最热评价”列的值，并将其存储在comment 变量中。
#使用SnowNLP 对comment 进行情感分析，获取情感分数，并将其存储在 sentiment 变量中
#使用之前定义的 get_sentiment_label 函数，根据 sentiment 分数为评论标注情感倾向标签，并将标签存储在 label 变量中。
#使用 standard_data.loc[index]来设置 standard_data DataFrame 中对应行的值。
#这里使用了当前循环的索引 index:编号从1开始而不是从开始，所以使用 index+1 作为编号。同时，也设置了酒店名称、评论内容、情感倾向标签和备注字段

from snownlp import SnowNLP
import pandas as pd
data = pd.read_csv('/root/travel/hotel/hotel_comment.csv')

# 定义情感倾向标注函数
def get_sentiment_label(sentiment):
    if sentiment >= 0.7:
        return '正向'
    elif sentiment >0.4:
        return '中性'
    else:
        return '负向'

#创建一个空的DataFranstandard_data，它有五个列:'编号'、'酒店名称’、'最热评价'、'情感倾向'和'备注'
standard_data = pd.DataFrame(columns=['编号','酒店名称','最热评价','情感倾向','备注'])
for index,row in data.iterrows():
    comment = row['最热评价']
    sentiment = SnowNLP(comment).sentiments
    label = get_sentiment_label(sentiment)
    standard_data.loc[index]=[index+1, row['酒店名称'], comment, label, '']

#存储标注结果
print(standard_data.head())
standard_data.to_csv('/root/travel/hotel/standard.csv', index=False, encoding='utf8')
