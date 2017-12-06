import pandas as pd
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dframe_list = pd.io.html.read_html(url)
print(dframe_list)

dframe = dframe_list[0]
print(dframe)

print(dframe.columns)


