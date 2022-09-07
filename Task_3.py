# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N  до N
a=int(input('введите число'))
# list=[]
# i=a
# while i!=-a:
#     list.append(int(-i))
#     i-=1
# print (list)
for i in range(-a,a+1):
    print(i,end=' ')