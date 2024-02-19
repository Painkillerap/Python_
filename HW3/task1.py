# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
#
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
#
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0


# def pack_backpack(items, max_weight):
#     possible_items = []
#     for item, weight in items.items():
#         if weight <= max_weight:
#             possible_items.append(item)
#             max_weight -= weight
#     return possible_items


backpack = {}
for key, value in items.items():
    if max_weight - value >= 0:
        backpack[key] = value
        max_weight = max_weight - value

# maxBagPack = {}
# for key, value in items.items():
#     if max_weight - value >= 0:
#         maxBagPack[key] = value
#         max_weight = max_weight - value
# print(maxBagPack)
# items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
# max_weight = 10
# print(pack_backpack(items, max_weight))
