import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")

x_values = [2.9, 2.99, 2.999, 3.0, 3.001, 3.01, 3.1]

f_values = [x for x in x_values]
g_values = [3 * x for x in x_values]
h_values = [f + g for f, g in zip(f_values, g_values)]

table = pd.DataFrame({
    "x": x_values,
    "f(x)=x": f_values,
    "g(x)=3x": g_values,
    "h(x)=f(x)+g(x)": h_values
})

table

x = np.linspace(-7, 7, 100)

f = x
g = 3 * x
h = f + g

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=x")
plt.plot(x, g, label="g(x)=3x")
plt.plot(x, h, label="h(x)=f(x)+g(x)=3x")
plt.scatter([2], [6], label="x=2, h=6")

plt.title("Предел суммы функций")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert h[0] == f[0] + g[0]


x_values = [1.9, 1.99, 1.999, 2.0, 2.001, 2.01, 2.1]

f_values = [x for x in x_values]
g_values = [x + 2 for x in x_values]
h_values = [f * g for f, g in zip(f_values, g_values)]

table = pd.DataFrame({
    "x": x_values,
    "f(x)=x": f_values,
    "g(x)=x+2": g_values,
    "h(x)=f(x)*g(x)": h_values
})

table


x_values = [0.5, 0.9, 0.99, 1.0, 1.01, 1.1, 1.5]

y_values = [(3 * x) / x for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "y=(3x)/x": y_values
})

table


x_values = [2.5, 2.9, 2.99, 2.999, 3.001, 3.01, 3.1, 3.5]

y_values = []

for x in x_values:
    y = (x ** 2 - 4) / (x - 2)
    y_values.append(y)

table = pd.DataFrame({
    "x": x_values,
    "y": y_values
})

table


x_left = np.linspace(-1, 2.99, 200)
x_right = np.linspace(3.01, 6, 200)

y_left = (x_left**2 - 9) / (x_left - 3)
y_right = (x_right**2 - 9) / (x_right - 3)

plt.figure(figsize=(7, 4))
plt.plot(x_left, y_left)
plt.plot(x_right, y_right)
plt.scatter([3], [6], facecolors="none", edgecolors="black", label="предел = 6")

plt.title("Неопределённость 0/0 и предел")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

x_values = [2.9, 2.99, 3.01, 3.1]

original_values = [(x ** 2 - 9) / (x - 3) for x in x_values]
simple_values = [x + 3 for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "исходная функция": original_values,
    "упрощённая x+2": simple_values
})

table


epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
metric = [0.55, 0.68, 0.78, 0.85, 0.90, 0.93, 0.95, 0.96, 0.965, 0.968]

plt.figure(figsize=(7, 4))
plt.plot(epochs, metric, marker="o")
plt.axhline(0.97, linestyle="--", label="возможный предел 0.97")

plt.title("Метрика модели приближается к пределу")
plt.xlabel("Эпоха")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

assert metric[-1] > metric[0]


summary = [
    "Предел суммы равен сумме пределов",
    "Предел произведения равен произведению пределов",
    "Предел частного можно считать, если знаменатель не стремится к нулю",
    "Неопределённость 0/0 часто можно упростить",
    "Пределы помогают понять поведение функций и моделей"
]

for item in summary:
    print("-", item)

assert len(summary) == 5


