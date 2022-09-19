# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
num=int(input('введите число '))
composition=[]
summ=0
for i in range(1,num+1):
    temp=(1+1/i)**i
    composition.append(temp)
    summ+=temp
print (composition) 
print (summ)

# 2 способ (другая запись)
# num=int(input('введите число '))
# list=[round((1+1/i)**i,5) for i in range(1,n+1)]
# print(f'Список:{list}')
# print(f'Сумма чисел списка: {round(sum(list),5)}')
# except ValueError:
# print('Вводить необходимо только целое число')