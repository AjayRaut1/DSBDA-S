import pandas as pd
import numpy as numpy
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("titatic.csv")
df

df.describe()

df.shape

df.size

df.isnull().sum()

df['Age'] = df['Age'].fillna(35)
df = df.dropna()
df.isnull.sum()

df.dtypes

df.info()

sns.distplot(df['Pclass'])

sns.distplot(df['Age'])

sns.distplot(df['Age'],bins=40)

sns.distplot(df['Age'],bins=20, kde=False, rug=True)

sns.jointplot(x=df['Age'], y=df['Fare'], kind='scatter')

sns.jointplot(x=df['Age'], y=df['Fare'], kind='hex')

sns.pairplot(df)

sns.barplot(x=df['Sex'], y=df['Fare'])

sns.countplot(df['Pclass'])

sns.distplot(df['Fare'], hist=True)