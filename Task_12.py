#  Напишите программу, которая принимает на вход число N и
#   выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
import random
num=int(input('введите число'))
x=1
print (x, end="")
for i in range(num-1):
    x*=(-3)
    print(x, end=" ") # 2 способ print((-3)**i,end=" "), т.е. -3 в степени i