import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Библиотеки подключены")


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)

f = np.ones_like(x) * 7
df = np.zeros_like(x)

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=7")
plt.plot(x, df, label="f'(x)=0")

plt.title("Производная константы")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert np.all(df == 0)


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)

f = 3 * x + 2
df = np.ones_like(x) * 3

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=3x+2")
plt.plot(x, df, label="f'(x)=3")

plt.title("Производная линейной функции")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert df[0] == 3


x = np.linspace(-4, 4, 200)

f = x ** 2
df = 2 * x

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=x²")
plt.plot(x, df, label="f'(x)=2x")

plt.title("Производная функции x²")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert len(f) == len(df)


x = np.linspace(-4, 4, 200)

f = x ** 3
df = 3 * x ** 2

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=x³")
plt.plot(x, df, label="f'(x)=3x²")

plt.title("Производная функции x³")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert np.min(df) >= 0


x = np.linspace(-4, 4, 200)

f = 4 * x ** 2
df = 8 * x

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=4x²")
plt.plot(x, df, label="f'(x)=8x")

plt.title("Производная функции с коэффициентом")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert len(f) == len(df)


x = np.linspace(-4, 4, 200)

f = x ** 2 + 3 * x
df = 2 * x + 3

plt.figure(figsize=(7, 4))
plt.plot(x, f, label="f(x)=x²+3x")
plt.plot(x, df, label="f'(x)=2x+3")

plt.title("Производная суммы")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

assert len(f) == len(df)


points = [-3, -2, -1, 0, 1, 2, 3]

f_values = [x ** 2 + 3 * x for x in points]
df_values = [2 * x + 3 for x in points]

table = pd.DataFrame({
    "x": points,
    "f(x)=x²+3x": f_values,
    "f'(x)=2x+3": df_values
})

table



points = [-3, -2, -1, 0, 1, 2, 3]

for x in points:
    derivative = 2 * x + 3

    if derivative > 0:
        message = "функция растёт"
    elif derivative < 0:
        message = "функция убывает"
    else:
        message = "возможная точка экстремума"

    print("x =", x, "| f'(x) =", derivative, "|", message)


    rules = [
    "Производная константы равна 0",
    "Производная x равна 1",
    "Производная x² равна 2x",
    "Производная x³ равна 3x²",
    "Производная суммы равна сумме производных",
    "Производная помогает понять рост и убывание функции"
]

for rule in rules:
    print("-", rule)

assert len(rules) == 6




