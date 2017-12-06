import numpy as np
import pandas as pd
import subprocess

## data sample
# !cat lec25.csv

dframe = pd.read_csv('lec25.csv')
print(dframe)

dframe1 = pd.read_csv('lec25.csv', header = None)
print(dframe1)
 
dframe2 = pd.read_table('lec25.csv', sep = ',', header = None)
print(dframe2)

dframe3 = pd.read_csv('lec25.csv', header = None, nrows = 2)
print(dframe3)

mytextdata = dframe.to_csv('mytextdata_out.csv')
cat_text = "cat mytextdata_out.csv"
subprocess.call( cat_text, shell = True)

# show file 
import sys
dframe.to_csv(sys.stdout)

# _0_1_2_3...
dframe.to_csv(sys.stdout, sep = '_')
# 0 1 2 3 ...
dframe.to_csv(sys.stdout, sep = '\t')

"""
 '\t' tab区切りに編集しているのでdframe -> dframe2 を使うか
定義し直す
"""
dframe2.to_csv(sys.stdout, columns = [0, 1, 2])





