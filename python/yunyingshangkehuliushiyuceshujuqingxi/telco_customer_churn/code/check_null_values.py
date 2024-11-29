import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

# data = pd.read_csv('./Telco_Customer_Churn.csv')
data = pd.read_csv('/root/service/telco_customer_churn/Telco_Customer_Churn.csv')
# print(data.isnull().sum())

data_not_null = data[~data.isnull().any(axis=1)]
data_not_null['TotalCharges'] = data_not_null.apply(
    lambda row: row['MonthlyCharges'] if row['TotalCharges'] == ' '
    else row['TotalCharges'], axis=1
)
data_not_null = data_not_null.dropna()
data_not_null['TotalCharges'] = data_not_null['TotalCharges'].astype(float)
data_not_null.to_csv('/root/service/telco_customer_churn/result/check_null_values.csv',index=False)