# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
col=int(input('введите количество элементов списка '))
list=[]
for i in range(col):
    temp=random.randint(0,10)
    list.append(temp)
print (list)

summ=0
for i in range(len(list)):
    if i%2!=0:
        summ+=list[i]
print ('cумма элементов на нечётных позициях равна ', summ)        
