# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# 
from re import I
num=int(input('введите целое число '))
strBinary=""
while num >1:
    ost=num%2
    num=num//2
    strBinary+=str(ost)
    if num==1: strBinary+=str(num)
result=strBinary[-1]
for i in range(1,len(strBinary)):
    result+=strBinary[-(i+1)]
print(result)
 

# 2 способ
#from re import I
# num=int(input('введите целое число '))
# binaryNum=[]
# while num >1:
#     ost=num%2
#     num=num//2
#     binaryNum.append(ost)
#     if num==1: binaryNum.append(num)
# for i in range(int(len(binaryNum)/2)):
#     temp=binaryNum[i]
#     binaryNum[i]=binaryNum[-(i+1)]
#     binaryNum[-(i+1)]=temp
# list=str(binaryNum[0])
# for i in range(1,len(binaryNum)):
#     list+=str(binaryNum[i])
# print (list)
