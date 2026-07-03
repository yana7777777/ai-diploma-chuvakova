import numpy as np
import matplotlib.pyplot as plt

print("Библиотеки подключены")

x = np.linspace(-10, 10, 200)
y = x ** 2

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Степенная функция y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert len(x) == len(y)

x = np.linspace(-10, 10, 200)
y = x ** 3

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Кубическая функция y = x³")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert y[0] < 0
assert y[-1] > 0


x = np.linspace(0, 10, 15, 25)
y = np.sqrt(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Функция корня y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert np.min(y) >= 0


x = np.linspace(-5, 5, 200)
y = 2 ** x

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Показательная функция y = 2ˣ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert np.all(y > 0)


x = np.linspace(0.1, 11, 15, 20)
y = np.log(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Логарифмическая функция y = log(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert len(x) == len(y)


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Функция y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert np.max(y) <= 1.01
assert np.min(y) >= -1.01


x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.cos(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y)
plt.title("Функция y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

assert np.max(y) <= 1.01
assert np.min(y) >= -1.01


x = np.linspace(-2 * np.pi, 2 * np.pi, 200)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")

plt.legend()
plt.grid(True)
plt.title("Сравнение sin(x) и cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

assert len(x) == 200
assert np.max(y_sin) <= 1.01 and np.min(y_sin) >= -1.01
assert np.max(y_cos) <= 1.01 and np.min(y_cos) >= -1.01



x = np.linspace(0.1, 10, 150)

y_linear = x
y_square = x ** 2
y_log = np.log(x)
y_exp = 2 ** x

plt.figure(figsize=(9, 6))
plt.plot(x, y_linear, label="y = x")
plt.plot(x, y_square, label="y = x²")
plt.plot(x, y_log, label="y = log(x)")
plt.plot(x, y_exp, label="y = 2ˣ")

plt.title("Сравнение элементарных функций")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

summary = [
    "Линейная функция растет равномерно",
    "Квадратичная растет быстрее линейной",
    "Логарифм растет медленно",
    "Экспонента растет быстрее всех"
]

for item in summary:
    print("-", item)

assert len(summary) == 4


