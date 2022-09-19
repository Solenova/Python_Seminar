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
    list[i],list[j]=list[j],list[i]      # поменять местами элементы
print (list) 

# 2 способ
# import random
# list=[]
# for i in range(col):
#     temp=random.randint(-50,50)
#     list.append(temp)
# print (list) 
# random.shuffle(list)          # метод перемешивания элементов случайным образом
# print (list)