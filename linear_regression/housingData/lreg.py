import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn import linear_model

brain_df = pd.read_fwf('brain_body.txt')
x_values = brain_df[['Brain']]
y_values = brain_df[['Body']]
print(x_values)
print(y_values)

# instance
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# Brain vs. Body
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()

