# coding: utf-8
from pyspark.ml.regression import LinearRegression

from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors

"""
Spark2.0で，Data Frame APIの活用(RDDよりも計算が速い)

$ spark-submit Spark_LinearRegression.py
"""

if __name__ == "__main__":

    # SparkSessionの作成
    spark = SparkSession.builder.config("spark.sql.warehouse.dir", "~/work/temp").appName("LinearRegression").getOrCreate()

    # Read the data, MLLib用のフォーマットに変換
    inputLines = spark.sparkContext.textFile("/Users/usui/work/python/DataScience/regression.txt")
    data = inputLines.map(lambda x: x.split(",")).map(lambda x: (float(x[0]), Vectors.dense(float(x[1]))))

    # RDDをDataFrameに変換
    colNames = ["label", "features"]
    df = data.toDF(colNames)

    # Dataを訓練データとテストデータに分割する
    trainTest = df.randomSplit([0.5, 0.5])
    trainDF = trainTest[0]
    testDF = trainTest[1]

    # 線形回帰モデルを作成する
    lir = LinearRegression(maxIter = 10, regParam = 0.3, elasticNetParam = 0.8)
    
    # 訓練データを用いて，モデルを訓練する
    model = lir.fit(trainDF)

    # テスト用のデータの特徴値に線形回帰モデルを適用して，予測を行う
    fullPredictions = model.transform(testDF).cache()

    # fullpredictionsから，予測値(predictions)と正解値(labels)を取り出す
    predictions = fullPredictions.select("prediction").rdd.map(lambda x: x[0])
    labels = fullPredictions.select("label").rdd.map(lambda x: x[0])

    # predictionsとlabelsを紐付ける
    predictionAndLabel = predictions.zip(labels).collect()

    # 各点の予測値と実際の値を出力する
    for prediction in predictionAndLabel:
        print(prediction)

    # stop session
    spark.stop()
