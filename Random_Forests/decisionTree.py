# coding: utf-8
import numpy as np
import pandas as pd
from sklearn import tree

"""
graphvizで決定木を作る(pipとbrew で graphviz をinstall)
slkearn は，決定木を扱うために全てのデータを数値化する必要がある．
categorical data -> dummy data に変換.


[pydot関係]
http://ukichang.hatenablog.com/entry/2016/06/21/011008

"""
 
input_file = "/Users/usui/work/python/DataScience/PastHires.csv"
df = pd.read_csv(input_file, header = 0)
# print(df.head())

# map() でDataFrameを書き換える
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Interned'] = df['Interned'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)

d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print(df.head())


# 決定木の構築用，特徴量
features = list(df.columns[0:6])
print("特徴量 =", features)

# 構築
y = df["Hired"]
X = df[features]
# instance, training
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)


"""
plot decision tree

[pydotplus]
https://stackoverflow.com/questions/38176472/graph-write-pdfiris-pdf-attributeerror-list-object-has-no-attribute-writ
"""
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus

import graphviz

dot_data = StringIO()
tree.export_graphviz(clf, out_file = dot_data,
                     feature_names = features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("./graph.pdf")
Image(graph.create_png())

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data = df[0:6])
plt.figure()

sns.violinplot(data = df[0:6])


"""
Ensemble with Random Forest 

"""
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators = 10)
clf = clf.fit(X, y)

# Predict employment of an employed 10-year veteran 
print("clf.predict([[10, 1, 4, 0, 0, 0]]) =", clf.predict([[10, 1, 4, 0, 0, 0]]))

# ...and an unemployed 10-year veteran
print("clf.predict([[10, 0, 4, 0, 0, 0]]) =", clf.predict([[10, 0, 4, 0, 0, 0]]))
print(clf.predict([[10, 0, 4, 0, 0, 0]]))
# plt.scatter(X[:, 0], X[:, 1], c = y)

plt.show()
