# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num=int(input('введите количество чисел негафибоначчи '))
# def negafib(n):
#     if n ==1: return 1
#     elif n==2: return -1
#     else: return (-1)**(n+1)*negafib(n-2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n==-1:
            return 1
    elif n >1:
        return fib(n-1) + fib(n-2)
    if n < -1:
        return fib(n+2)-fib(n+1)
print(fib(num))
list=[]
for e in range(-num,num+1):
    list.append(fib(e))
print (list)    
