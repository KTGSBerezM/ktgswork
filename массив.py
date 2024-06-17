#1
k, l = [], []
for i in range(1, 11):
    k.append(10 -i)
for i in range(1, 11):
    l.append(k[5] - k[i - 1])
print(k)
print(l)

#2
k, l = list(range(1, 11)), list(range(1, 11))

for i in range(1, 11):
    k[i - 1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i-1]
print(k)
print(l)
print(f'Количество отрицательных элементов массива l = {len([value for value in l if value < 0])}')

#3
k, l = list(range(1, 11)), list(range(1, 11))

for i in range(1, 11):
    k[i - 1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i - 1]
print(k)
print(l)
count_k = 0
for value in k:
    if value < 0:
        count_k += 1
count_l = 0
for value in l:
    if value < 0:
        count_l += 1
print(f'Количество отрицательных элементов = {count_k + count_l}')


count_k = len([value for value in k if value < 0])
count_l = len([value for value in l if value < 0])
print(f'Количество отрицательных элементов = {count_k + count_l}')