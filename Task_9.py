# Напишите программу, которая принимает на вход координаты двух точек и
#  находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from math import sqrt

x1=int(input('введите абсциссу точки А ='))
y1=int(input('введите ординату точки А = '))
x2=int(input('введите абсциссу точки В = '))
y2=int(input('введите ординату точки В = '))
d=sqrt((x2-x1)**2+(y2-y1)**2)
# d=((x2-x1)**2+(y2-y1)**2)**0.5
print(f'расстояние между точками А({x1},{y1}) и В({x2},{y2}) равно {round(d,2)}') 