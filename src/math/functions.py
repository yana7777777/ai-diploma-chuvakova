import numpy as np


def loss_function(x):
    return (x - 3) ** 2 + 2

def linear(x):
    return 2 * x + 1

def quadratic(x):
    return x ** 2

def cubic(x):
    return x ** 3

def sin_function(x):
    return np.sin(x)

def cos_function(x):
    return np.cos(x)

def exp_function(x):
    return np.exp(x)

def log_function(x):
    return np.log(x + 1)