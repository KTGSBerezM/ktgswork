a=1,2,3
b=str(a)
print(b)
print(type(b))

a=int(input('Введите число'))
if a%2==0:
    print(f'число {a} является четным')
else:
    print(f'число {a} является нечетным')



a=str(input('Введите строку'))
b=len(a)
print(f'Количество символов в строке: {b}')
