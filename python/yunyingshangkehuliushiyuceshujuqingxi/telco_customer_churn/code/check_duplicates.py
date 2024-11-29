import pandas as pd

data = pd.read_csv('/root/service/telco_customer_churn/result/check_null_values.csv')
print(data.duplicated(subset='customerID'))
print(data.duplicated(subset='customerID').sum())
data = data.drop_duplicates(subset='customerID')
data.to_csv('/root/service/telco_customer_churn/result/check_duplicates.csv', index = False)
