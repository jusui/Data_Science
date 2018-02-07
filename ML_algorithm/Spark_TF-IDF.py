# coding: utf-8
from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

"""
TF-IDF(Term Frequency:単語出現頻度, Inverse Documnet Frequency:逆文章頻度)
文章と単語の関係 = TF/DF

spark-submit Spark_TF-IDF.py
"""

# Sparkの設定
conf = SparkConf().setMaster("local").setAppName("SparkTFIDF")
sc = SparkContext(conf = conf)

# 文章の読み込み
rawData = sc.textFile("/Users/usui/work/python/DataScience/subset-small.tsv")
fields = rawData.map(lambda x: x.split("\t"))
documents = fields.map(lambda x: x[3].split(" "))

# 文章の名前を取り出す
documentNames = fields.map(lambda x: x[1])

# TFの計算，各文章の単語はハッシュ値として数値化される
hashingTF = HashingTF(100000) # ハッシュ値の上限
tf = hashingTF.transform(documents)

# IDFの計算
tf.cache()
idf = IDF(minDocFreq = 2).fit(tf)

# 各文章における各単語のTF*IDFを計算
tfidf = idf.transform(tf)

"""
既にRDDをsparseベクトルとして取得済み(https://spark.apache.org/docs/latest/mllib-data-types.html)
各TF*IDFの値は，各文章ごとにハッシュ値と関連付けて格納されている

今回のデータは，Abraham Lincoln Speech at Gettysburgの単語検索

"""

# Gettysburgのハッシュ値取得
gettysburgTF = hashingTF.transform(["Gettysburg"])
gettysburgHashValue = int(gettysburgTF.indices[0]) # 8748

# Gettysburgのハッシュ値に対応するTF*IDFのスコアを取りだし，各文章毎にRDDに格納
gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue]) # PythonRDD[10] at RDD at PythonRDD.scala:48

# 文章の名前とハッシュ値の関連付けを行う
zippedResults = gettysburgRelevance.zip(documentNames)
print(zippedResults)

# 最後に、　最大のTF*IDFを持つ文章を出力
print("Best document for Gettysburg is:")
print(zippedResults.max())
