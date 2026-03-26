#%%
import pandas as pd
df = pd.read_csv(r"C:\Users\barat\PycharmProjects\PythonProject\JupyterProject\customer_shopping_behavior.csv")

#%%
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
#%%

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
#%%

#CREATE A COLUMN FOR AGE_GROUP

labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
#%%
#CREATE COLUMN PURCHASE_FREQUENCY_DAYS

frequency_mapping = {
    'Fortnight':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every Three Months':90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
#%%
df=df.drop('promo_code_used',axis=1)
#%%


from sqlalchemy import create_engine

#MYSQL CONNECTION
username="root"
password="root"
host="localhost"
port="3306"
database="customer_behavior"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

#WRITE DATAFRAME TO MYSQL
table_name ="mytable" #CHOOSE ANY TABLE NAME
df.to_sql(table_name, engine, if_exists="replace", index=False)

#READ BACK SAMPLE
pd.read_sql("SELECT * FROM mytable LIMIT 5;", engine)
#%%

#%%
