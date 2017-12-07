import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.datasets import laod_boston

"""

Linear Regression

Step 1: データの準備
Step 2: ひとまず可視化
Step 3: 最小二乗法の数学的な背景
Step 4: Numpyを使った単回帰
Step 5: 誤差について
Step 6: scikit-learnを使った重回帰分析
Step 7: 学習（Training）と検証Validation）
Step 8: 価格の予測
Step 9 : 残差プロット

"""

# ====================
# データの準備
# ====================
print(bonston.DESCR)
