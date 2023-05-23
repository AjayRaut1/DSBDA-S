import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(iris.csv)
df

df.shape

df.describe()

df.info()

df.dtypes

sns.distplot(df['sepal_length'], hist=True)

sns.distplot(df['sepal_width'], hist=True)

sns.distplot(df['petal_length'], hist=True)

sns.distplot(df['petal_width'], hist=True)

sns.boxplot(df['sepal_length'])

sns.boxplot(df['sepal_width'])

sns.boxplot(df['petal_length'])

sns.boxplot(df['petal_width'])

sns.boxplot(data=df, x=df['sepal_length'], y=df['species'])

sns.boxplot(data=df, x=df['sepal_width'], y= df['species'])

sns.boxplot(data=df, x=df['petal_length'], y= df['species'])

sns.boxplot(data=df, x=df['petal_width'], y= df['species'])
