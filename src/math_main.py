scores = [60, 75, 80, 50, 95, 70]

print("Оценки:", scores)
print("Количество оценок:", len(scores))

assert len(scores) == 6


scores = [60, 75, 80, 50, 95, 70]

average_score = sum(scores) / len(scores)

print("Средний балл:", average_score)

assert average_score > 0



scores = [60, 75, 80, 50, 95, 70]

max_score = max(scores)
min_score = min(scores)

print("Максимум:", max_score)
print("Минимум:", min_score)

assert max_score == 95
assert min_score == 50


scores = [60, 75, 80, 50, 95, 70]

high_scores = []

for score in scores:
    if score > 60:
        high_scores.append(score)

print("Оценки выше 80:", high_scores)

assert len(high_scores) == 4


user = {
    "name": "Галя",
    "city": "Самара",
    "id": 20,
    "status": "new",
    "rating": 4.5
}

print(user)
print("Имя:", user["name"])
print("id:", user["id"])

assert user["city"] == "Самара"


users = [
    {"name": "Галя", "city": "Самара", "id": 20, "status": "new", "rating": 4.5},
    {"name": "Петр", "city": "Москва", "id": 21, "status": "active", "rating": 3.8},
    {"name": "Ольга", "city": "Казань", "id": 22, "status": "blocked", "rating": 4.9},
    {"name": "Иван", "city": "Уфа", "id": 23, "status": "active", "rating": 3.2}
]

for user in users:
    print(user)

assert len(users) == 4


filtered_items = []

for user in users:
    if user["city"] == "Казань" and user["status"] == "blocked":
        filtered_items.append(user)

print(filtered_items)

assert len(filtered_items) >= 1


sorted_users = sorted(users, key=lambda x: x["id"])

print(sorted_users)

assert len(sorted_users) == 4
assert sorted_users[0]["id"] < sorted_users[-1]["id"]


items = [1, 2, 3, 2, 4, 5, 3, 6, 1]

unique_values = set(items)

print("Уникальные значения:", unique_values)

assert len(unique_values) >= 2


users = [
    {"name": "Галя", "city": "Самара", "id": 20, "status": "new", "rating": 4.5},
    {"name": "Петр", "city": "Москва", "id": 21, "status": "active", "rating": 3.8},
    {"name": "Ольга", "city": "Казань", "id": 22, "status": "blocked", "rating": 4.9},
    {"name": "Иван", "city": "Уфа", "id": 23, "status": "active", "rating": 3.2}
]

filtered = [user for user in users if user["status"] == "active"]

sorted_users = sorted(filtered, key=lambda x: x["id"], reverse=True)

best = sorted_users[0] if sorted_users else None

print("Лучший результат:", best)

assert best is not None
assert best["rating"] >= 3.2


