import numpy as np
import matplotlib.pyplot as plt

X_POINTS = np.array([1, 2, 3, 4, 5, 6])
"""
Just for the sake of simplicity, we are using 
y=1.1*x +- <delta>
"""
Y_POINTS = np.array([1.14, 2.092, 3.42, 4.67, 5.93, 6.17])
plt.scatter(X_POINTS, Y_POINTS)
plt.show()
