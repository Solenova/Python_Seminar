# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
col=int(input('введите количество элементов '))
list=[]
listOst=[]
for i in range(col):
    list.append(round(random.uniform(-10.0, 25.0),5))   # задали случайным образом элементы списка
    listOst.append(abs(list[i]-int(list[i])))       # выделили дробную часть и поместили в список listOst

max=listOst[0]
min=listOst[0]
for i in range(col):              # этим циклом находим максимальный и минимальный элементы списка остатков
    if listOst[i]>max: max=listOst[i]
    if listOst[i]<min: min=listOst[i]
print (list) 
print(listOst)
print ('max= ',max)
print('min= ', min)
print ('max-min= ',max-min) 
