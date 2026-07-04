import numpy as np
import matplotlib.pyplot as plt

from src.math.functions import loss_function, linear, quadratic, cubic

def show_loss_graph():
    x = np.linspace(-2, 8, 300)
    y = loss_function(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="loss(x) = (x - 3)² + 2")
    plt.scatter([3], [2], label="минимум")
    plt.legend()
    plt.grid(True)
    plt.title("Функция ошибки")
    plt.show()

def show_linear():
    x = np.linspace(-5, 5, 100)
    y = linear(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Линейная функция")
    plt.show()

def show_quadratic():
    x = np.linspace(-5, 5, 100)
    y = quadratic(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Квадратичная функция")
    plt.show()

def show_cubic():
    x = np.linspace(-3, 3, 100)
    y = cubic(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Кубическая функция")
    plt.show()