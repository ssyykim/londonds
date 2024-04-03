from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('test.csv', delimiter=',', skip_header=0)

print(data)