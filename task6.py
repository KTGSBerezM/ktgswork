#Задача #1. Проверка вхождения подстроки
str_ =  "Строка с цифрой 1"
is_substr = "Строка" in str_
print("В строке есть слово Строка?", is_substr)

#Задача #2
number = 12
condition_1 = number % 2 == 0
condition_2 = number % 3 == 0
if condition_1 and condition_2:
    print('Число кратно 2 и 3')
else:
    print('Число не (кратно 2 и 3)')

#Задача #3
mount = 12
bad_condition = \
    mount == 12 or \
    mount == 1 or \
    mount == 2
good_condition = mount in [12, 1, 2]
if good_condition:
    print("Зима!!!")

#Задача #4
hour = 7
bad_condition = (6 <= hour) and (hour < 12)
good_condition = 6 <= hour < 12
if good_condition:
    print("Утро!!!")

#Задача #5
list_ = [5, 6, 7, 8, 9]
result = (4 in list_) and (8 in list_)
print(result)