
from sklearn.linear_model import LinearRegression
import numpy as np


# A simple function to train and return a linear Regression model
def train_model():
    #example data: simply y = 2x model
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) #y is the label

    model = LinearRegression()
    model.fit(X, y)
    return model

# A simple function to train and return a linear Regression model
def train_marks_model():
    #example data: simply y = 2x model
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [20]])
    y = np.array([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5])

    model = LinearRegression()
    model.fit(X, y)
    return model

# Function to make predictions
def make_predictions(model, x_new):
    return model.predict(np.array([[x_new]]))