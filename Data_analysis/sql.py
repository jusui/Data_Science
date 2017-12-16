# encoding utf-8
import sqlite3
import pandas as pd

# データベースと接続するために、Connectionオブジェクトを作る必要がある
con = sqlite3.connect('sakila.db')

# sql
sql_query = 'select * from customer'

# DF
# df = pd.read_sql(sql_query, con)

# print(df)

# DataFrameを作る関数
def sql_to_df(sql_query):
    df = pd.read_sql(sql_query, con)

    return df

query = ''' select first_name, last_name 
        from customer'''

print(sql_to_df(query))

sql_to_df('select country_id from city')

# distinct : Unique
sql_to_df('select distinct(country_id) from city')

# 条件①
query = ''' select * from customer where store_id = 1 '''
print(sql_to_df(query).head())

# 条件②
query = ''' select * from customer where first_name = 'MARY' '''
print(sql_to_df(query).head())

# 複数条件
query = ''' select * from film where release_year = 2006 and rating='R' '''
print(sql_to_df(query).head())

# OR
query = ''' select * from film where rating = 'PG' or rating = 'R' '''
print(sql_to_df(query).head())



"""

Lec 102 
応用編

"""

# 人数を数える
query = ''' select count(customer_id) from customer '''
print(sql_to_df(query).head())


'''
=== MEMO ===

基本的な使い方は、以下の様な感じ.

SELECT 列名, まとめる関数(列名)
FROM テーブル名
WHERE ・・・


'''

# Wild Card : %

# Initial M of First_Name
query = ''' select * from customer where first_name like 'M%'; '''
print(sql_to_df(query).head())

# last_name の最後が ~ingの人.
query = ''' select * from customer where last_name like '_ING' '''
print(sql_to_df(query).head())

# A or Bから始まる人.
query = ''' select * from customer where first_name GLOB '[AB]*' '''
print(sql_to_df(query).head())



# order by で並べ替え
query = ''' select * from customer order by last_name ; '''
print(sql_to_df(query).head())

# 逆順(Z,Y,X,...A) : DESC
query = ''' select * from customer order by last_name DESC; '''
print(sql_to_df(query).head())


# group by でまとめる.
# 店ごとに，人数を調査
query = ''' select store_id, count(customer_id) from customer group by store_id; '''
print(sql_to_df(query).head())
