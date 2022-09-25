# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N  до N
a=int(input('введите число'))
# list=[]
# i=a
# while i!=-a:
#     list.append(int(-i))
#     i-=1
# print (list)

#2 method
# for i in range(-a,a+1):
#     print(i,end=' ')

#Задание к 6 семинару(улучшение кода)
print([i for i in range(-a,a+1)])
