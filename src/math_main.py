import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")

x_values = [1.5, 1.9, 1.99, 2.0, 2.01, 2.1, 2.5]

y_values = []

for x in x_values:
    y_values.append(3 * x)

table = pd.DataFrame({
    "x": x_values,
    "y = 3x": y_values
})

table

x = np.linspace(0, 6, 100)
y = 3 * x

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="y = 3x")
plt.scatter([2], [6], label="точка x=2, y=6")

plt.title("Предел на примере y = 3x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

assert 3 * 2 == 6


left_x = [1.9, 1.99, 1.999]
right_x = [2.1, 2.01, 2.001]

left_y = [2 * x for x in left_x]
right_y = [2 * x for x in right_x]

table = pd.DataFrame({
    "x слева": left_x,
    "y слева": left_y,
    "x справа": right_x,
    "y справа": right_y
})

table


x_values = [2.5, 2.9, 2.99, 3.0, 3.01, 3.1, 3.5]
y_values = [x ** 2 for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "y = x²": y_values
})

table


x = np.linspace(-1, 5, 200)
y = x ** 2

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="y = x²")
plt.scatter([3], [9], label="x=3, y=9")

plt.title("Предел на примере y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

assert 3 ** 2 == 9


x_values = [0.7, 0.9, 0.99, 0.999, 1.003, 1.03, 1.3, 1.8]

y_values = []

for x in x_values:
    y = (x ** 2 - 4) / (x - 2)
    y_values.append(y)

table = pd.DataFrame({
    "x": x_values,
    "y": y_values
})

table


x_left = np.linspace(-1, 1.99, 100)
x_right = np.linspace(2.01, 4, 100)

y_left = (x_left ** 2 - 4) / (x_left - 2)
y_right = (x_right ** 2 - 4) / (x_right - 2)

plt.figure(figsize=(7, 4))
plt.plot(x_left, y_left)
plt.plot(x_right, y_right)
plt.scatter([2], [4], facecolors='none', edgecolors='black', label="предел = 4")

plt.title("Функция не определена в x=2, но предел есть")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()


epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loss = [0.9, 0.75, 0.6, 0.48, 0.38, 0.30, 0.23, 0.18, 0.14, 0.10]

plt.figure(figsize=(7, 4))
plt.plot(epochs, loss, marker='o', linestyle='-')

plt.title("Ошибка модели стремится к 0")
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

assert loss[-1] < loss[0]


summary = [
    "Предел показывает, к чему стремится функция",
    "К точке можно приближаться слева и справа",
    "Функция может иметь предел, даже если не определена в точке",
    "Пределы нужны для понимания производной и оптимизации",
    "В AI идея предела связана с уменьшением ошибки модели"
]

for item in summary:
    print("-", item)

assert len(summary) == 5


