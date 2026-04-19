from data_utils import find_by_name, filter_by_value, count_items

user = [
    {"id": 1, "name":"Антон", "surname":"Иванов", "age":25, "city": "Москва"},
    {"id": 2, "name":"Олег", "surname":"Петров", "age":45, "city": "Ярославль"},
    {"id": 3, "name":"Гриша", "surname":"Сидоров", "age":55, "city": "Самара"},
    {"id": 4, "name":"Рустам", "surname":"Еськов", "age":75, "city": "Ульяновск"}
]

print(find_by_name(user, "Антон"))
print(filter_by_value(user, "city", "Самара"))
print(count_items(user))