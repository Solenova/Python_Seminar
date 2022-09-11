#  Реализуйте алгоритм перемешивания списка.
import random
col=int(input('введите количество элементов '))
list=[]
for i in range(col):
    temp=random.randint(-50,50)
    list.append(temp)
print (list) 
for i in range(col):
    j=random.randint(0,col)
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
print (list) 
