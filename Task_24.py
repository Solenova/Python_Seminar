# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
import random
col=int(input('введите количество элементов '))
list=[]
for i in range(col):
    temp=random.randint(-col,col)
    list.append(temp)
print (list) 
file1 = open("input.txt", "r") # получим объект файла
lines = file1.readlines()   # считываем все строки
file1.close # закрываем файл
if int(lines[0])<=col and int(lines[1])<=col:
    composition=list[int(lines[0])]*list[int(lines[1])]
    print(composition)
else: print('один из номеров позиций(или оба) больше элементов последовательности')

