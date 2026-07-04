import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")

x = np.linspace(-4, 4, 200)
y = x ** 2

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="f(x)=x²")
plt.scatter([0], [0], label="минимум")

plt.title("Функция с минимумом")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

assert min(y) >= 0

x = np.linspace(-3, 7, 300)
y = (x - 3) ** 2 + 2

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="f(x)=(x-3)²+2")
plt.scatter([3], [2], label="минимум x=3, y=2")

plt.title("Смещённый минимум функции")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

assert 2 == (3 - 3) ** 2 + 2


import numpy as np
import pandas as pd

x_values = [1, 2, 3, 4, 5, 6, 7]

y_values = [(x - 3) ** 2 + 2 for x in x_values]

table = pd.DataFrame({
    "x": x_values,
    "f(x)": y_values
})

table

def derivative(x):
    return 2 * (x - 3)

points = [-1, 0, 1, 2, 3, 4, 5]
derivatives = [derivative(x) for x in points]

table = pd.DataFrame({
    "x": points,
    "f'(x)": derivatives
})

table

def derivative(x):
    return 2 * (x - 3)

points = [-1, 0, 1, 2, 3, 4, 5]

for x in points:
    d = derivative(x)

    if d < 0:
        message = "функция убывает"
    elif d > 0:
        message = "функция растёт"
    else:
        message = "критическая точка"

    print("x =", x, "| производная =", d, "|", message)


    x = np.linspace(-4, 4, 200)
y = -x ** 2 + 9

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="f(x)=-x²+9")
plt.scatter([0], [9], label="максимум")

plt.title("Функция с максимумом")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

assert (-0 ** 2 + 9) == 9


def f(x):
    return (x - 2) ** 2 + 1

def df(x):
    return 2 * (x - 2)

x_current = -3
learning_rate = 0.2

history_x = []
history_y = []

for step in range(15):
    history_x.append(x_current)
    history_y.append(f(x_current))

    gradient = df(x_current)
    x_current = x_current - learning_rate * gradient

print("Финальное x:", x_current)
print("Финальное f(x):", f(x_current))

assert abs(x_current - 2) < 1


x = np.linspace(-4, 6, 200)
y = f(x)

plt.figure(figsize=(7, 4))
plt.plot(x, y, label="f(x)=(x-2)²+1")
plt.scatter(history_x, history_y, label="шаги оптимизации")

plt.title("Градиентный спуск приближается к минимуму")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

assert history_y[-1] < history_y[0]


summary = [
    "Оптимизация — это поиск лучшего значения",
    "Минимум функции важен для уменьшения ошибки модели",
    "Производная помогает понять направление движения",
    "Критическая точка возникает там, где производная равна 0",
    "Градиентный спуск двигается против направления роста функции"
]

for item in summary:
    print("-", item)

assert len(summary) == 5




