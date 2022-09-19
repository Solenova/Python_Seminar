# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
col=int(input('введите количество элементов списка '))
listNum=[]
for i in range(col):
    temp=random.randint(0,10)
    listNum.append(temp)
print (listNum)

def unique_numbers(numbers):
    unique=[]
    for i in numbers:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique

print(unique_numbers(listNum))

# 2 способ
# unique_numbers = list(set(listNum))
# print(unique_numbers)

#3 method
# numbers = [1, 2, 2, 3, 3, 4, 5]

# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)

#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)

#     return list_of_unique_numbers

# print(get_unique_numbers(numbers))