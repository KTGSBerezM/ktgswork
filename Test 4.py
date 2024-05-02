#tuple create
a=[1,2.1,3]
tuple(a)
b=tuple('abc')

a = (1, 1.1,'a',[4, 5, 6], {'a':1,'b':2},None,True)
a=()
b= tuple()
b=(1,)

#tuple retrive
a=[1,2.1,3]
tuple(a)
b=tuple('abc')

a=(1,1.1,'a')
print(a)
print((1,1.1,'a'))

a=(1,1.1,'a')
a[0]
a[1]
a[2]
a[3]
a[-1]
a[-2]
a[-3]
a[-4]

#tuple update
a=(1,1.1,'a')
a[0]='a'
a=(1,2,3)

#tuple delete
a=(1,1.1,'a')
del a[0]
del a

#tuple действия с кортежами
#кортежи можно складывать с кортежами
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)
a+=b
#кортежи можно умножать на целое число
a=(1,2,3)
b=2
c=a*b
print(c)
a*=b
#кортежи как и списки можно делать вложенными
a=(1,2,3)
b=((1,2,3),(4,5,6),(7,8,9))
#обращение ко вложенным кортежам ничем не отличается от обращения к вложенным спискам
b=((1,2,3),(4,5,6),(7,8,9))
b[0]
b[0][0]
b[-1][-1]

#tuple методы
help(tuple)
a=(1,2,1)
a.count(1)
a.index(2)

#tuple практические моменты
a=(1,2,[1,2,3])
a[2][0]=10
a=[1,2,3]
b=[1,2,a]
a[1]=20
print[b]

#словарь dict
#create dict
a={'a':1}
a={'a':1,'b':2}
a=dict([['a',1],['b',2]])
a=dict(a=1,b=2)

#dict составной тип данных
a={}
b=dict()
a=dict([['a',1],['b',2]])
a=dict((('a',1),('b',2)))
a={1:'a',1.1:'b','c':3.(1,2):[1,2,3], frozenset({1,2}):{1,2},4:{1:2,3:4},print:4}
a={'a':1,'a':3,'b':2}

#dict retrive(read)
a={'a':1,'b':1.1}
print(a)
print({'a':1,'b':1.1})

a={'a':1,'b':1.1,1:'abc'}
a[0]
a['a']
a['b']
a[1]
var_b='b'
a[var_b]

a={'a':1,'b':1.1,1:'abc'}
a.get('a')
a.get(0)
a.get(0,'a')

#dict update(добавление)
a={'a':1,'b':1.1}
a['c']=2

a={'a':1,'b':1.1}
a.setdefault('c',2)

a={'a':1,'b':1.1}
a.update({'a':10,'c':'abc'})

#dict update(изменение)
a={'a':1,'b':1.1}
a['b']=2

a={'a':1,'b':1.1}
a.setdefault('b',2)

#dict delete(удаление)
a={'a':1,'b':1.1}
del a['a']
del a

a={'a':1,'b':1.1}
a.clear()
a={'a':1,'b':1.1}
a.popitem()
a={'a':1,'b':1.1}
a.pop('a')

#dict(действия с объектами)
a={'a':1,'b':1.1}
b={'a':1,'b':{'c':10}}

b={'a':1,'b':{'c':10}}
b['b']
b['b']['c']

#dict(методы)
help(dict)
a={'a':1,'b':1.1}
a.copy()
a.values()
a.keys()
a.items()
dict.fromkeys(['a','b','c'],10)

#dict(практические моменты)
products={'апельсин':{'цена':100,'вес':0.5},'банан':{'цена':110,'вес':1}}
products['апельсин']['цена']
products['банан']
banan=products['банан']
banan['вес']