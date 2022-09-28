# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

def step(x):
    return x**2

def summ(x,y):
    return x+y

listNum=[x for x in range(10,100)]
list_quadre=list(filter(lambda x: x%9==0,listNum))
print (sum (list(map(lambda x: x**2, list_quadre))))