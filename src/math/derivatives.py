import numpy as np

def loss_derivative(x):
    return 2 * (x - 3)

def linear_derivative(x):
    return 2

def quadratic_derivative(x):
    return 2 * x

def cubic_derivative(x):
    return 3 * x ** 2

def sin_derivative(x):
    return np.cos(x)

def cos_derivative(x):
    return -np.sin(x)

def exp_derivative(x):
    return np.exp(x)

def log_derivative(x):
    return 1 / (x + 1)