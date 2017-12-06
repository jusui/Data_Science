import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# NFLのデータをサンプルとして使います。
import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
# webbrowser.open(website)

nfl_frame = pd.read_clipboard()
print(nfl_frame)
print(nfl_frame.columns)
# print(nfl_frame['First NFL Season'])
# print('nfl_frame.Team')
# nfl_frame[['Team', 'First Season']]
# print(nfl_frame)
# DataFrame(nfl_frame, columns = ['Team', 'First NFL Season', 'Stadium'])

nfl_frame['Stadium'] = np.arange(6)
print(nfl_frame)

stadium = Series(["Levi's stadium", 'AT&T Stadium'], index = [4, 0])
print(stadium)
nfl_frame['Statidum'] = stadium
print(nfl_frame)

del nfl_frame['Stadium']
print(nfl_frame)

data = {'City':['SF', 'LA', 'NYC'], 'Population':[837000, 3880000, 840000]}
print(data)
city_frame = DataFrame(data)
print(city_frame)

