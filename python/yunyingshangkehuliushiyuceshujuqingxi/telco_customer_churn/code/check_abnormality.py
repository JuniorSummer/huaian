import pandas as pd

data = pd.read_csv('/root/service/telco_customer_churn/result/check_duplicates.csv')
print(data.info())
print(data.describe())

for col in data.columns:
    # 不同列有不同的判别方式
    if col == 'SeniorCitizen':
        outliers = data[(data['SeniorCitizen'] != 0) & (data['SeniorCitizen'] != 1)]
        if not outliers.empty:
            print('在{}发现异常值：{}'.format(col, outliers))
            data = data[(data['SeniorCitizen'] == 0) | (data['SeniorCitizen'] == 1)]
    elif col == 'MonthlyCharges' or col == 'TotalCharges':
    # elif col in ['MonthlyCharges','TotalCharges']:
        mean = data.describe().loc['mean', col]
        # mean = data[col].describe().mean()
        std = data.describe().loc['std', col]
        # std = data[col].describe().std()
        lower_bound = mean - 2.5 * std
        upper_bound = mean + 2.5 * std
        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        if not outliers.empty:
            print('在{}发现异常值：{}'.format(col, outliers))
            outliers = data[(data[col] > lower_bound) & (data[col] < upper_bound)]

data.to_csv('/root/service/telco_customer_churn/result/check_abnormality.csv', index = False)
