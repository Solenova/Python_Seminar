# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
num=int(input('введите число '))
composition=[]
temp=1
for i in range(num):
    temp*=(i+1)
    composition.append(temp)
print (composition) 

# 2 способ (простой, но малоприменимый, т.к. введенные числа не остаются в памяти)
# num=int(input('введите число '))
# a=1
# for i in range(1,num+1):
#     a*=i
#     print(a,end=" ")
# print()    