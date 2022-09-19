# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
a=input('введите число ')
temp=0
summ=0
for i in range(len(a)):
    if a[i]!='.' and a[i]!='-':
        temp=int(a[i])
        summ+=temp
print (summ)        

#2 способ
# a=float(input('введите число '))
# while a % 1 >0:
#     a*=10
# summ=0
# while a>0:
#     summ+=a%10
#     a//=10    
# print (int(summ))    

# 3 способ
namber=input('Введите число')
sum=0
for i in number:
    if i.isdigit():     # метод распознает число или текст
        sum+=int(i)
print(int(sum))        