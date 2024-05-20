#Цикл for
for value in collection:
#Пример использования
for i in range(3):
    print(i + 1, "шаг цикла")
    print("Первый цикл закончился!")

a = {1: 'x' , 2: 'y', 3: 'z'}
for index, value in a.items():
    print(f'"Позиция: {index} -> Значение: {value}"')

#Перебор значений коллекции с помощью for
#Список list
for value in[1, 2, 3, 4, 5]:
    print(value)
#Кортеж tuple
for value in(1, 2, 3, 4, 5):
    print(value)
#Множество set
for value in{1, 2, 3, 4, 5}:
    print(value)

#Функция range()
range(start, stop, step)
#Пример использования
range(10)# Генерация последовательности чисел от 0 до 9
range(1, 11)# Генерация последовательности чисел от 1 до 10
range(1, 11, 2)# Генерация последовательности чисел от 1 до 10 с шагом 2
range(10, 0, -1)# Генерация последовательности чисел от 10 до 1 с шагом -1
#Примеры функции range()
print(range(10)) # объект типа range
print(list(range(10))) # список целых чисел от 0 до 9 включительно
print(tuple(range(1, 11))) # кортеж целых чисел от 1 до 10 включительно
print(list(range(1, 11, 2))) # список целых нечетных чисел от 1 до 9 включительно
print(tuple(range(10, 0, -1))) # range так же поддерживает отрицательный шаг

#Именование переменной в цикле
#Пример использования _ в цикле:
for _ in range(5): # Просто выполнить цикл 5 раз
print("Hello World!")

#Рефакторинг кода
numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
print("Сумма чисел:", total)

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Сумма чисел:", total)

#Использование функции enumearte в python
#Перебор кортежей индекс-значение
for tuple_ in enumerate(["а","б","в"]):
    print(tuple_)
#Множественная распаковка для получекния индекса и значения
for pos, value in enumerate("абв", start=1):
    print("Позиция:", pos, "->", "Значение:", value)

#Цик while
#Формат записи цикла while
while условие:
#Пример использования цикла while
count = 0
while count < 5:
    print("Значение count:", count)
    count += 1

sum_ = 0
input_number = int(input("Введите число: "))
while input_number != 0:
    sum_ += input_number
    input_number = int(input("Введите число: "))
print("Ответ:", sum_)

#Бесконечный цикл while
num = 10
while num > 0:
    print(num)
    