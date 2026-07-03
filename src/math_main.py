import numpy as np
import matplotlib.pyplot as plt

print("Библиотеки подключены")


x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

y = 2 * x + 1

print("x =", x)
print("y =", y)

assert len(x) == len(y)

x = np.linspace(-10, 10, 100)

y = 2 * x + 1

plt.figure(figsize=(8, 5))
plt.plot(x, y)

plt.title("Линейная функция y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)

plt.show()


x = np.linspace(-10, 10, 100)

y1 = x
y2 = 4 * x
y3 = -x

plt.figure(figsize=(7, 4))

plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = 4x")
plt.plot(x, y3, label="y = -x")

plt.legend()
plt.grid(True)

plt.title("Влияние коэффициента k")

plt.show()



y1 = x
y2 = x + 5
y3 = x - 5

plt.figure(figsize=(7, 4))

plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = x + 5")
plt.plot(x, y3, label="y = x - 5")

plt.legend()
plt.grid(True)

plt.title("Влияние коэффициента b")

plt.show()




x = np.linspace(-10, 10, 100)

y = x ** 2

plt.figure(figsize=(7, 4))

plt.plot(x, y)

plt.title("Квадратичная функция y = x²")

plt.grid(True)

plt.show()



x = np.linspace(-8, 8, 80)

y1 = x ** 2
y2 = 2 * x ** 2
y3 = x ** 2 + 10

plt.figure(figsize=(8, 5))

plt.plot(x, y1, label="y = x²")
plt.plot(x, y2, label="y = 2x²")
plt.plot(x, y3, label="y = x² + 10")

plt.legend()
plt.grid(True)

plt.title("Изменение квадратичной функции")

plt.show()


x = np.linspace(-4, 4, 80)

y = x ** 2

print("Минимум:", np.min(y))
print("Максимум:", np.max(y))

assert np.min(y) >= 0




metrics = {
    "epoch": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "loss": [0.9, 0.75, 0.62, 0.51, 0.42, 0.35, 0.29, 0.24, 0.20, 0.17]
}

plt.figure(figsize=(7, 4))
plt.plot(metrics["epoch"], metrics["loss"], 'b-o', linewidth=2, markersize=6)
plt.title("График обучения модели")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

assert len(metrics["epoch"]) == 10


summary = [
    "Функции используются в AI",
    "Графики помогают анализировать данные",
    "matplotlib используется для визуализации",
    "Линейные и квадратичные функции — основа дальнейшей математики"
]

for item in summary:
    print("-", item)

assert len(summary) == 4

print("\nВЫВОД:")
print("Проект показывает базовые навыки Python для анализа данных:")
print("- Работа с функциями")
print("- Визуализация графиков")
print("- Оптимизация через градиентный спуск")
print("- Структурирование кода в модули")
print("- Работа с Git и GitHub")

