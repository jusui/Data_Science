# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

eta_01_list = [0.9503, 0.9479, 0.9448, 0.9452, 0.948, 0.9483, 0.9454, 0.9486, 0.9509, 0.9507]
eta_01_array = np.array(eta_01_list)
print("eta_01_array :", eta_01_array)
print(eta_01_array.mean())
print(eta_01_array.std())

eta_02_list = [0.9501, 0.9513, 0.9489, 0.9501, 0.9523, 0.9512, 0.9521, 0.947, 0.9481, 0.9494]
eta_02_array = np.array(eta_02_list)
print("eta_02_array :", eta_02_array)
print(eta_02_array.mean())
print(eta_01_array.std())

eta_03_list = [0.9428, 0.9501, 0.9418, 0.9422, 0.9446, 0.9476, 0.9434, 0.9471, 0.9472, 0.9465]
eta_03_array = np.array(eta_03_list)
print("eta_03_array :", eta_03_array)
print(eta_03_array.mean())
print(eta_01_array.std())

eta_04_list = [0.9353, 0.9404, 0.9399, 0.9344, 0.9343, 0.9382, 0.9397, 0.9431, 0.9336, 0.9353]
eta_04_array = np.array(eta_04_list)
print("eta_04_array :", eta_04_array)
print(eta_04_array.mean())
      
eta_05_list = [0.9276, 0.9209, 0.9244, 0.9141, 0.9075, 0.9262, 0.9247, 0.9278, 0.9245, 0.9327]
eta_05_array = np.array(eta_05_list)
print("eta_05_array :", eta_05_array)
print(eta_05_array.mean())
      
eta_06_list = [0.9151, 0.9184, 0.9079, 0.9193, 0.9182, 0.919, 0.8881, 0.9159, 0.9162, 0.9209]
eta_06_array = np.array(eta_06_list)
print("eta_06_array :", eta_06_array)
print(eta_06_array.mean())
      
eta_07_list = [0.8671, 0.8817, 0.9122, 0.898, 0.8859, 0.8852, 0.9041, 0.895, 0.8842, 0.8785]
eta_07_array = np.array(eta_07_list)
print("eta_07_array :", eta_07_array)
print(eta_07_array.mean())
      
eta_08_list = [0.8799, 0.877, 0.858, 0.8931, 0.869, 0.8935, 0.888, 0.8786, 0.891, 0.8952]
eta_08_array = np.array(eta_08_list)
print("eta_08_array :", eta_08_array)
print(eta_08_array.mean())

eta_09_list = [0.8583, 0.8773, 0.8543, 0.8662, 0.8496, 0.8555, 0.865, 0.8566, 0.8497, 0.8805]
eta_09_array = np.array(eta_09_list)
print("eta_09_array :", eta_09_array)
print(eta_09_array.mean())

eta_array = eta_01_array + eta_02_array + eta_03_array + eta_04_array + eta_05_array + eta_06_array + eta_07_array + eta_08_array + eta_09_array
print(eta_array)

y = [eta_01_array, eta_02_array, eta_03_array, eta_04_array, eta_05_array, eta_06_array, eta_07_array, eta_08_array, eta_09_array]
print(y)

y_mean = [eta_01_array.mean(), eta_02_array.mean(), eta_03_array.mean(), eta_04_array.mean(), eta_05_array.mean(), eta_06_array.mean(), eta_07_array.mean(), eta_08_array.mean(), eta_09_array.mean()]
print(y_mean)

y_std = [eta_01_array.std(), eta_02_array.std(), eta_03_array.std(), eta_04_array.std(), eta_05_array.std(), eta_06_array.std(), eta_07_array.std(), eta_08_array.std(), eta_09_array.std()]

x = [x for x in np.arange(0.1, 1, 0.1)]
print(x)

plt.errorbar(x, y_mean, yerr = y_std, fmt = 'o')
plt.title("accuracy vs. eta")
plt.xlabel("Learning rate[eta]")
plt.ylabel("MNIST accuracy")
plt.show()
