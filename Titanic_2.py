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
print('Age.value_counts() = {}:'.format(titanic_df['Age'].value_counts()))

### KDE plot
# 1つに描画 FacetGrid()
fig = sns.FacetGrid(titanic_df, hue = 'Sex', aspect = 4)
# KDEはでーたから推定して描画する
fig.map(sns.kdeplot, 'Age', shade = True)
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))
fig.add_legend()

## for child
fig = sns.FacetGrid(titanic_df, hue = 'person', aspect = 4)
# KDEはでーたから推定して描画する
fig.map(sns.kdeplot, 'Age', shade = True)
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))
fig.set(ylim = (0, 0.09))
fig.add_legend()

## for 
fig = sns.FacetGrid(titanic_df, hue = 'Pclass', aspect = 4)
# KDEはでーたから推定して描画する
fig.map(sns.kdeplot, 'Age', shade = True)
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))
fig.set(ylim = (0, 0.04))
fig.add_legend()

plt.figure()

## Column deck に注目してみると、NaN多いので取り除く
deck = titanic_df['Cabin'].dropna()
print(deck)

# deck のいち文字目だけ取り出す
levels = []
for level in deck:
    levels.append(level[0])

print(levels)

cabin_df  = DataFrame(levels)
cabin_df.columns = ['Cabin']
print(cabin_df)

sns.countplot('Cabin', data = cabin_df, palette = 'winter_d', \
              order = sorted(set(levels)))


plt.figure()


# hist 見ると、Tがおかしいので、外れ値 T を取り除く
cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.countplot('Cabin', data = cabin_df, palette = 'summer', order = sorted(set(cabin_df.Cabin)))
plt.figure()


## 次に、どの港(Embarked)で乗船したかを確認する
sns.countplot('Embarked', data = titanic_df, hue = 'Pclass')
plt.figure()


from collections import Counter
count_embarked = Counter(titanic_df.Embarked)
print(count_embarked)
print(titanic_df.Embarked.value_counts())

plt.show()

