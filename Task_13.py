# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой
str1=(input('введите первую строку '))
str2=(input('введите вторую строку '))

if len(str1)<len(str2):
    print(str2.count(str1))
else:
    print(str1.count(str2))           

# 2 способ (не работает, если символы в строке одинаковые)
# a='pyt'
# b='pythonpythonpython'
# for i in range(0, len(b)-len(a)):
#     if b[i:i+len(a)]==a:  #к номеру i прибавляет количество символов в 1 строке
#         count+=1
#   print(count)      