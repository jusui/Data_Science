import pandas as pd
from pandas import Series, DataFrame

"""
Titanic dataset

Paramters
------------------
SibSp : 兄弟姉妹と同乗
Parch : 両親と同乗


"""

## Read Titanic dataset
titanic_df = pd.read_csv('train.csv')
print(titanic_df)

# summary
print(titanic_df.info())

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## count sex
sns.countplot('Sex', data = titanic_df)
plt.figure()

## クラス
sns.countplot('Sex', data = titanic_df, hue = 'Pclass')
plt.figure()

## Sex
sns.countplot('Pclass', data = titanic_df, hue = 'Sex')
plt.figure()

## Age子供ならchild, それ以外は性別
def male_female_child(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis = 1)
print(titanic_df)

sns.countplot('Pclass', data = titanic_df, hue = 'person')
plt.figure()

titanic_df['Age'].hist(bins = 70)

print('titanic_df.mean() = {}:'.format(titanic_df['Age'].mean()))
# titanic_df.mean() 29.69911764705882: =
print('Age.value_counts() = {}:'.format(titanic_df['Age'].value_counts()))

plt.show()

