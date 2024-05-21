#Задача 8.1: Поиск суммы чисел вводимых с клавиатуры
total = 0
while True:
    num = int(input("Введите число:"))
    if num == 0:
        break
    if num > 0:
        total += num
print("Сумма положительных чисел:", total)

#Задача 8.2: Придумать 3 примера итераций
#По ключу
a = {'chocolate': {'kind': 'milk', 'price': 70},
     'cookie': {'kind': 'oatmeal', 'price': 110},
     'sweets': {'kind': 'lollipops', 'price': 140}
     }
for value in a.keys():
    print(value)

#По значению
fruites = {'chocolate': {'kind': 'milk', 'price': 70},
     'cookie': {'kind': 'oatmeal', 'price': 110},
     'sweets': {'kind': 'lollipops', 'price': 140}
           }
for value in fruites.values():
    print(value)

#По паре ключ - значение
fruites = {'chocolate': {'kind': 'milk', 'price': 70},
     'cookie': {'kind': 'oatmeal', 'price': 110},
     'sweets': {'kind': 'lollipops', 'price': 140}
           }
for value in fruites.items():
    print(value)