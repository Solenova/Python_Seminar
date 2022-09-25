# НОД двух чисел
from re import A


num_first=int(input('введите 1 число '))
num_two=int(input('введите 2 число '))

#NOD с помощью рекурсии
def NOD(a,b):
    if a%b==0:
        return b
    else:
        return NOD (b,a%b)    

# 2 method
def NOD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
nod=NOD(num_first,num_two)
print (nod)

# 3 method
# a=20
# b=58
# if a<b:
#     a,b=b,a             #поменяли местами
# while b!=0:
#     a,b=b,a%b
# print (a)

# 4 method
# c=gsd(a,b)        # встроеная функция 