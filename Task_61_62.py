# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
#  Реализовать программу с использованием функции filter. 
#  Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример^
#  - 8 11 0 -23 140 1 => 11 -23
# 2. Дан список, вывести отдельно буквы и цифры.
a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
num='-8 11 0 -23 140 1'
data=list(map(int,num.split()))

def f(x):
    if x>9 and x<100 or x>-100 and x<-9:
        return(x)

res=list(filter(lambda x: f(x),data)) 
print (res)
# print(list(filter(lambda x: 9<abs(x)<100,data)))  # краткая запись вышеперечисленного
# print(*filter(lambda x: len(str(abs(int(x))))==2, input().split())) # еще короче запись

a = ( "a", 'b', '2', '3' ,'c')

inp=list(map(str,input('insert text: ').split()))   # вводим строку с клавиатуры
res=list(filter(lambda x: x.isdigit(),a)) 
resNam=list(filter(str.isdigit,a))              # встроеная функция str
resStr=list(filter(str.isalpha,a))
print (res)
print (resNam)
print (resStr)