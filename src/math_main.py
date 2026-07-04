import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")


x = np.linspace(-4, 4, 200)
y = x ** 2

plt.figure(figsize=(7, 4))
plt.plot(x, y)

plt.title("Функция y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert len(x) == len(y)


x_values = [2.8, 2.9, 3.0, 3.1, 3.2]
y_values = [x ** 2 for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "y = x²": y_values
})

table


def f(x):
    return x ** 2

x0 = 3
h = 0.001

derivative = (f(x0 + h) - f(x0)) / h

print("Приближённая производная в x=3:", derivative)

assert derivative > 5.9
assert derivative < 6.1

def numerical_derivative(func, x, h=0.001):
    return (func(x + h) - func(x)) / h

points = [-3, -2, -1, 0, 1, 2, 3]

derivatives = [numerical_derivative(f, point) for point in points]

table = pd.DataFrame({
    "x": points,
    "приближённая производная": derivatives,
    "точная производная 2x": [2 * point for point in points]
})

table


x = np.linspace(-4, 4, 200)

y = x ** 2
dy = 2 * x

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="y = x²")
plt.plot(x, dy, label="y' = 2x")

plt.title("Функция и производная")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()



x = np.linspace(-1, 5, 300)

def f(x):
    return x ** 2

x0 = 3
y0 = f(x0)
slope = 2 * x0

tangent = slope * (x - x0) + y0

plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label="y = x²")
plt.plot(x, tangent, label="касательная в x=3")
plt.scatter([x0], [y0], label="точка касания")

plt.title("Касательная к графику")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert slope == 6


x_points = [-3, -2, -1, 0, 1, 2, 3]

for point in x_points:
    derivative_value = 2 * point

    if derivative_value > 0:
        message = "функция растёт"
    elif derivative_value < 0:
        message = "функция убывает"
    else:
        message = "точка минимума или горизонтальная касательная"

    print("x =", point, "| производная =", derivative_value, "|", message)


    x = np.linspace(-4, 4, 200)

loss = x ** 2
gradient = 2 * x

plt.figure(figsize=(8, 5))
plt.plot(x, loss, label="loss = x²")
plt.plot(x, gradient, label="gradient = 2x")
plt.scatter([0], [0], label="минимум ошибки")

plt.title("Ошибка модели и производная")
plt.xlabel("параметр модели")
plt.ylabel("значение")
plt.legend()
plt.grid(True)
plt.show()

assert min(loss) >= 0



summary = [
    "Производная показывает скорость изменения функции",
    "Производная связана с наклоном касательной",
    "Численную производную можно посчитать через маленький шаг h",
    "Если производная положительная, функция растёт",
    "Производная нужна для оптимизации и обучения AI-моделей"
]

for item in summary:
    print("-", item)

assert len(summary) == 5

