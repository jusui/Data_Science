import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


"""
Titanic dataset

Paramters
------------------
SibSp : 兄弟姉妹と同乗
Parch : 両親と同乗


"""

titanic_df = pd.read_csv('train.csv')

## 乗客が独身が既婚か調べる
titanic_df['Alone'] = titanic_df.Parch + titanic_df.SibSp
print(titanic_df['Alone'])

# 変形 (Warning!!)
titanic_df['Alone'].loc[titanic_df['Alone'] > 0] = 'With Family'
titanic_df['Alone'].loc[titanic_df['Alone'] == 0] = 'Alone'

print(titanic_df.head())

## 既婚かどうか
sns.countplot('Alone', data = titanic_df, palette = 'Blues')
plt.figure()

## Survivor とは (Survived(0,1))
titanic_df['Survivor'] = titanic_df.Survived.map({0:'no', 1:'yes'})
sns.countplot('Survivor', data = titanic_df, palette = 'Set1')
# plt.figure()

## Age子供ならchild, それ以外は性別
def male_female_child(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis = 1)
print(titanic_df)

## 生存率 factorplot() class 
sns.factorplot('Pclass', 'Survived', data = titanic_df, order = [1,2,3])

sns.factorplot('Pclass', 'Survived', hue = 'person', data = titanic_df, order = [1, 2, 3], aspect = 2)


# Survivor vs. Age
sns.lmplot('Age', 'Survived', data = titanic_df)

# Pclass で層別化
sns.lmplot('Age', 'Survived', hue = 'Pclass', data = titanic_df, palette = 'winter', \
           hue_order = [1, 2, 3])

# 更に見やすくする
generations = [10, 20, 40, 60, 80]
sns.lmplot('Age', 'Survived', hue = 'Pclass', data = titanic_df, palette = 'winter', \
           hue_order = [1, 2, 3], x_bins = generations)

# Sex
sns.lmplot('Age', 'Survived', hue = 'Sex', data = titanic_df, palette = 'winter', \
           x_bins = generations)

plt.show()

