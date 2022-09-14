# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
col=int(input('введите количество элементов списка '))
list=[]
for i in range(col):
    temp=random.randint(0,10)
    list.append(temp)
print (list)
listComp=[]  
if col%2==0: rang=col/2 
else: rang= int(col/2)+1    
for i in range(rang):
    composition=list[i]*list[len(list)-i-1]
    listComp.append(composition)
print(listComp)    
