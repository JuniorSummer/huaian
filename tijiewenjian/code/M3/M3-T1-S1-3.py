import pandas as pd
da = pd.read_csv('/root/travel/hotel/district.csv')
#筛出5星级酒店
da_five_star = da[da['酒店类型']=='五星级']
# 分数平均
score_mean = da_five_star['评分'].mean()
#.format(score_mean):这是字符串格式化方法。它将score_mean 的值插入到字符串中的 {} 占位符位置。
print('/root/travel/hotel/五星级酒店平均分为:\n{}'.format(score_mean))
