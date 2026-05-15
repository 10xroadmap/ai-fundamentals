import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# Just for the sake of simplicity, we are using y=1.1*x +- <delta>
X_POINTS = np.array([[1], [2], [3], [4], [5], [6]])
Y_POINTS = np.array([1.14, 2.092, 3.42, 4.67, 5.93, 6.17])
# Linear Regression: Finding "best fit" line
linear = LinearRegression()
'''
X_POINTS: Training data
Y_POINTS: Target values
fit() method calculates the optimal parameters m(slope) and c(intercept)
for y=m*x+c
'''
linear.fit(X_POINTS, Y_POINTS)
# Now let's find output when input is 2.5
input = np.array([[2.5]])
prediction = linear.predict(input)
print(prediction) # [2.82040952]
