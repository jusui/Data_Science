# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from neural_network import NeuralNetwork
from neural_network import TestMethods
import sys
import unittest


def MSE(y, Y):
    return np.mean((y - Y) ** 2)


if __name__ == '__main__':
    """
    外部リソースのURLには、2013年のワシントンD.C.におけるバイクレンタル数のデータが入っています。
    このデータをニューラルネットワークを使用して学習し、ある日付のレンタル数を予測するモデルを構築してください。
    """

    data_path = 'hour.csv'
    rides = pd.read_csv(data_path) # (17379, 17)
    print(rides.head())
    print(rides.shape)

    """
    データセット
    [期間] 2011年1月1日から2012年12月31日まで2年間
    [cnt] 1時間毎のライダーの数を計測
    [caual/registered] 未登録/登録済で分けている
    """
    # 最初の10日間(24hour * 10 days)をプロット
    rides[:24*10].plot(x = 'dteday', y = 'cnt')
    plt.figure()


    """
    ダミー化
    季節などのカテゴリカル変数を，モデルに追加する.(0, 1)
    pd.get_dummies()
    """
    dummy_fields = ['season', 'weathersit', 'mnth', 'hr', 'weekday']
    for each in dummy_fields:
        dummies = pd.get_dummies(rides[each], prefix=each, drop_first=False)
        rides = pd.concat([rides, dummies], axis=1)

    fields_to_drop = ['instant', 'dteday', 'season', 'weathersit', 
                      'weekday', 'atemp', 'mnth', 'workingday', 'hr']
    data = rides.drop(fields_to_drop, axis=1)
    print(data.head())

    """
    Scaling target variables
    """
    quant_features = ['casual', 'registered', 'cnt', 'temp', 'hum', 'windspeed']
    # store scaling in a dictionary so we can convert back later
    scaled_features = {}
    for each in quant_features:
        mean, std = data[each].mean(), data[each].std()
        scaled_features[each] = [mean, std]
        data.loc[:, each] = (data[each] - mean) / std
        # print(data)


    """
    Splitting the data into training, testing, and validation sets
    
    トレーニング後に，テストデータに最後の約21日分を利用する．
    予測と正解の比較に用いる
    """
    # Save data for approximately the last 21 days
    test_data = data[-21*24:] # (504, 59)

    # Now remove the test data from the data set
    data = data[:-21*24] # (16875, 59)

    # Separate the data into features(16875, 56) and targets(16875, 3)
    target_fields = ['cnt', 'casual', 'registered']
    features, targets = data.drop(target_fields, axis = 1), data[target_fields]
    # test_features(504, 56), test_targets(504, 3)
    test_features, test_targets = test_data.drop(target_fields, axis = 1), test_data[target_fields]

    # 時系列データセットを2つに分ける. 1->training, 2->validating
    train_features, train_targets = features[:-60*24], targets[:-60*24]
    val_features, val_targets = features[-60*24:], targets[-60*24:]


    
    # if __name__ == '__main__':
    inputs = np.array([[0.5, -0.2, 0.1]])
    targets = np.array([[0.4]])
    test_w_i_h = np.array([[0.1, -0.2],
                           [0.4, 0.5],
                           [-0.3, 0.2]])

    test_w_h_o = np.array([[0.3],
                           [-0.1]])
    
    suite = unittest.TestLoader().loadTestsFromModule(TestMethods())
    unittest.TextTestRunner().run(suite)
    
    ### set the hyperparametres here ###
    iterations = 5000
    learning_rate = 0.2
    hidden_nodes = 15
    output_nodes = 1

    N_i = train_features.shape[1]
    network = NeuralNetwork(N_i, hidden_nodes, output_nodes, learning_rate)

    losses = {'train':[], 'validation':[]}
    for ii in range(iterations):
        # go through a random batch fo 128 records from the training data set
        batch = np.random.choice(train_features.index, size = 128)
        X, y = train_features.ix[batch].values, train_targets.ix[batch]['cnt']

        network.train(X, y)

        # printing out the training progress
        train_loss = MSE(network.run(train_features).T, train_targets['cnt'].values)
        val_loss = MSE(network.run(val_features).T, val_targets['cnt'].values)
        sys.stdout.write("\rProgress: {:2.1f}".format(100 * ii/float(iterations)) \
                         + "% ... Training loss: " + str(train_loss)[:5] \
                         + " ... Validation loss: " + str(val_loss)[:5])
        sys.stdout.flush()

        losses['train'].append(train_loss)
        losses['validation'].append(val_loss)

        
    plt.plot(losses['train'], label = 'Training loss')
    plt.plot(losses['validation'], label = 'Validation loss')
    _ = plt.ylim()
    plt.figure()

    
    """
    check out your predictions
    """
    fig, ax = plt.subplots(figsize=(8,4))

    mean, std = scaled_features['cnt']
    predictions = network.run(test_features).T*std + mean
    ax.plot(predictions[0], label='Prediction')
    ax.plot((test_targets['cnt']*std + mean).values, label='Data')
    ax.set_xlim(right=len(predictions))
    ax.legend()

    dates = pd.to_datetime(rides.ix[test_data.index]['dteday'])
    dates = dates.apply(lambda d: d.strftime('%b %d'))
    ax.set_xticks(np.arange(len(dates))[12::24])
    _ = ax.set_xticklabels(dates[12::24], rotation=45)
    
    plt.show()
