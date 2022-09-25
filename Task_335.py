# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num=int(input('введите количество чисел негафибоначчи '))

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n==-1:
        return 1
    elif n >1:
        return fib(n-1) + fib(n-2)
    if n < -1:
        return fib(n+2)-fib(n+1)
list=[]
# for e in range(-num,num+1):
#     list.append(fib(e))
# print (list)    

# Семинар 6 улучшение кода
print ([fib(i) for i in range (-num,num+1) ])