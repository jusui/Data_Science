import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples = 500, centers = 4, random_state = 8, cluster_std = 2.4)
print(X)
print('X[:, 0] ={}'.format(X[:, 0]))
print('X[:, 1] ={}'.format(X[:, 1]))
print(y)

# scatter plot the points
plt.figure(figsize = (10, 10))
plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'jet')


from sklearn.tree import DecisionTreeClassifier


# 描画のための関数
def visualize_tree (classifier, X, y, boundaries = True, xlim = None, ylim = None):
    '''
    決定木の可視化
    Inputs : 分類モデル, X, y, optional x/y limits.
    Outputs : Meshgrid を使った決定木の可視化

    '''
    # fit を使ったモデルの構築
    classifier.fit(X, y)

    # 軸を自動調整
    if xlim is None:
        xlim = (X[:, 0].min() - 0.1, X[:, 0].max() + 0.1)

    if ylim is None:
        ylim = (X[:, 1].min() - 0.1, X[:, 1].max() + 0.1)



    x_min, x_max = xlim
    y_min, y_max = ylim    


    # meshgrid
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), \
                         np.linspace(y_min, y_max, 100))
        

    # 分類器の予測をZとして保存
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    # meshgrid を使って，整形する
    Z = Z.reshape(xx.shape)

    # 分類器ごとに，色付け
    plt.figure(figsize = (10, 10))
    plt.pcolormesh(xx, yy, Z, alpha = 0.2, cmap = 'jet')
    
    # 訓練データを描画
    plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'jet')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    def plot_boundaries(i, xlim, ylim):
        '''
        境界線を書き込む

        '''
        if i < 0:
            return

        tree = classifier.tree_
        print(tree)

        # 境界を描画するため，再帰的に呼び出す
        if tree.feature[i] == 0:
            plt.plot([tree.threshold[i],  tree.threshold[i]], ylim, '-k')
            plot_boundaries(tree.children_left[i], [xlim[0], tree.threshold[i]], ylim)
            plot_boundaries(tree.children_right[i], [tree.threshold[i], xlim[1]], ylim)

        elif tree.feature[i] == 1:
            plt.plot(xlim, [tree.threshold[i], tree.threshold[i]], '-k')
            plot_boundaries(tree.children_left[i], xlim[0], [tree.threshold[i]], ylim)
            plot_boundaries(tree.children_right[i], xlim, [tree.threshold[i], ylim[1]])


        if boundaries:
            plot_boundaries(0, plt.xlim(), plt.ylim())



            
# model
clf = DecisionTreeClassifier(max_depth = 2, random_state = 0)

# vasualize
visualize_tree(clf, X, y)


# 深さを4 にしてみる
clf = DecisionTreeClassifier(max_depth = 4, random_state = 0)

# vasualize
visualize_tree(clf, X, y)
# max_depth 4 だと, overfit 気味


"""
Random Forest

過学習の問題を回避するための一つの方法が、ランダムフォレストです。

ランダムフォレストは、学習データの一部をランダムに選んで、決定木を作ります。これを繰り返すことによって、色々な種類の木が出来るので、汎化性能が下がるのを避けることが出来るわけです。

"""

from sklearn.ensemble import RandomForestClassifier

# インスタンスを作る. n_estimatorsは，作る木の数
clf = RandomForestClassifier(n_estimators = 100, random_state = 0)

# 境界線を描かないようにする
visualize_tree(clf, X, y, boundaries = False)


'''
Random Forest Regression

ランダムフォレストは、分類だけではなく、回帰にも使うことができます。

ダミーのデータを作って、試してみましょう。

'''

from sklearn.ensemble import RandomForestRegressor

x = 10 * np.random.rand(100)

def sin_model(x, sigma = 0.2):
    '''
    (大きな波 + 小さな波 + ノイズ) から成るダミーデータ
    '''

    noise = sigma * np.random.randn(len(x))

    return np.sin(5 * x) + np.sin(0.5 * x) + noise

# x から yを計算
y = sin_model(x)
print(y)

# plot
plt.figure(figsize = (16, 8))
plt.errorbar(x, y, 0.1, fmt = 'o')



# このデータを単純な線形回帰で予測しようとしても難しいのは、一目瞭然です。 
#そこで、ランダムフォレストを使って見ることにしましょう。 

# X, np.linspace() : 線形に等間隔な数列を生成する
xfit = np.linspace(0, 10, 1000)

# 回帰モデル
rfr = RandomForestRegressor(100)

# Train model
rfr.fit(x[:, None], y)

# predict model
yfit = rfr.predict(xfit[:, None])

# 実際の値
ytrue = sin_model(xfit, 0)

# plot
plt.figure(figsize = (16, 8))

plt.errorbar(x, y, 0.1, fmt = 'o')

plt.plot(xfit, yfit, '-r')
plt.plot(xfit, ytrue, '-k', alpha = 0.5)


plt.show()



