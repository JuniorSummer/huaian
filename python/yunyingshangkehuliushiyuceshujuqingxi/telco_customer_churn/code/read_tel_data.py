import pandas as pd

# data = pd.read_csv('./Telco_Customer_Churn.csv')
data = pd.read_csv('/root/service/telco_customer_churn/Telco_Customer_Churn.csv')
print(data.shape)
print(data.head(10))