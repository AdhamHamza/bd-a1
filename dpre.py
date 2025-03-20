import seaborn as sns
import pandas as pd 
import numpy as np
import subprocess
df=pd.read_csv("/home/doc-bd-a1/res_load.csv")

#data cleaning 
df.info()
df.isnull().sum()
#sns.histplot(df.Age)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Age'].isnull().sum()
df.columns
df=df.drop(['Cabin'],axis=1)
df.columns
len(df.Embarked)
df.Embarked.unique()
#sns.histplot(df.Embarked)
df.Embarked.mode()
df.Embarked[df.Embarked.isna()] = df.Embarked.mode()[0]
df.info()
# checking the duplicates of records 
df.duplicated().sum()
#data reduction 
df = df.drop(['Name','Ticket'],axis=1)

df.Embarked.unique()
df = pd.get_dummies(df, dtype=int)
#Discretization 
def categorize_age(age):
    if age < 18:
        return 'Child'
    elif age < 35:
        return 'Young Adult'
    elif age < 50:
        return 'Adult'
    else:
        return 'Senior'
df['Age_category_'] = df['Age'].apply(lambda x: categorize_age(x))
df = pd.DataFrame(df)
df.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)
print("DataFrame saved to res_dpre.csv")
subprocess.run(["python3", "eda.py", "/home/doc-bd-a1/res_dpre.csv"])