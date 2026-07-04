import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")

x = np.linspace(-4, 4, 200)
y = x ** 2

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Непрерывная функция y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert len(x) == len(y)

x = np.linspace(-2 * np.pi, 2 * np.pi, 300)
y = np.cos(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Непрерывная функция y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert np.max(y) <= 1.01
assert np.min(y) >= -1.01


x_left = np.linspace(-5, -0.1, 300)
x_right = np.linspace(0.1, 5, 300)

y_left = 1 / x_left
y_right = 1 / x_right

plt.figure(figsize=(7, 4))
plt.plot(x_left, y_left)
plt.plot(x_right, y_right)

plt.title("Функция с разрывом y = 1/x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


x_values = [-0.1, -0.2, -0.1, -0.04, 0.01, 0.1, 0.2, 1]

y_values = [1 / x for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "y = 1/x": y_values
})

table

x_left = np.linspace(-2, 1.99, 200)
x_right = np.linspace(2.01, 5, 200)

y_left = (x_left ** 2 - 4) / (x_left - 2)
y_right = (x_right ** 2 - 4) / (x_right - 2)

plt.figure(figsize=(7, 4))
plt.plot(x_left, y_left)
plt.plot(x_right, y_right)
plt.scatter([2], [4], facecolors="none", edgecolors="black", label="дырка")

plt.title("Функция с дыркой")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

x = np.linspace(-5, 5, 300)

y = []

for value in x:
    if value < 1:
        y.append(0)
    else:
        y.append(2)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Функция со скачком")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert min(y) == 0
assert max(y) == 2


x = np.linspace(-5, 5, 300)

y_smooth = x ** 2

y_jump = []
for value in x:
    if value < 0:
        y_jump.append(-1)
    else:
        y_jump.append(1)

plt.figure(figsize=(7, 4))
plt.plot(x, y_smooth, label="непрерывная: x²")
plt.plot(x, y_jump, label="разрывная: скачок")

plt.title("Сравнение непрерывной и разрывной функции")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smooth_loss = [2.5, 1.8, 1.2, 0.9, 0.7, 0.55, 0.45, 0.38, 0.33, 0.30]
jump_loss = [2.5, 1.5, 2.0, 0.8, 1.2, 0.6, 0.9, 0.4, 0.5, 0.3]

plt.figure(figsize=(7, 4))
plt.plot(epochs, smooth_loss, marker="o", label="плавное обучение")
plt.plot(epochs, jump_loss, marker="s", label="скачки ошибки")

plt.title("Плавное и нестабильное изменение ошибки")
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

assert smooth_loss[-1] < smooth_loss[0]


summary = [
    "Непрерывную функцию можно представить как плавный график",
    "Разрыв — это дырка, скачок или обрыв графика",
    "Функция 1/x имеет разрыв при x=0",
    "Функции с резкими скачками сложнее анализировать",
    "Непрерывность важна для производной, оптимизации и AI"
]

for item in summary:
    print("-", item)

assert len(summary) == 5


