import numpy as np
import pandas as pd
import matplotlib as plt
%matplotlib inline
import seaborn as sns

df = pd.read_csv('C:/titanic.csv')
df

df.info()

df.describe()

df.shape

df.size

df.isnull().sum()

sns.boxplot(df['Age'], df['Sex'])

sns.boxplot(df['Age'], df['Sex'], df['Survived'])

sns.countplot(x='Sex', data = df)

df['Survived'].value_counts().plot(kind='pie',autopct='%2f')

# OR 

sns.boxplot(data['Sex'], data["Age"], data["Survived"], palette = 'Set2').set_title('Plot for distribution of age with respect to each gender along with the information about whether they survived or not')
plt.show()