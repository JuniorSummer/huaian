import pandas as pd

data = pd.read_csv('/root/service/telco_customer_churn/result/check_abnormality.csv')
bool_cols = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity',
'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Churn']
for col in bool_cols:
    data[col] = data[col].map({'Yes': 1, 'No': 0, "No internet service": 101, "No phone service": 102})
data.to_csv('/root/service/telco_customer_churn/result/check_yes.csv', index=False)
