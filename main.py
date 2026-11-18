from src.load import load_raw

path = "data/raw/archive (3)/credit_risk_dataset.csv"

df = load_raw(path)

print(df.shape)
print(df.head())
print(df.dtypes)
print(df.info())
print(df.describe())

print(df["person_age"].max())
print(df["loan_int_rate"].isna().sum())
print(df["person_emp_length"].isna().sum())
print(df["person_age"].mean())