# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from itertools import count

col=int(input('Вы создаете справочник. Задайте количество людей в справочнике'))
# создаем справочник: запрашиваем имя и заносим в список, запрашиваем номер, состоящий из цифр, и записываем в др список
listName=[]
listNumber=[]
for i in range(col):
    temp=input ('Имя ')
    listName.append(temp.capitalize())
    while temp.isdigit()==False:
        temp=input('Введите номер телефона состоит из цифр ')
    listNumber.append(temp)

#распечатка справочника
for i in range(col):
    print( f"{listName[i]} ", end='')
    print( listNumber[i])

# Поиск номера в списке по заданному имени
req=input('Введите имя, чей номер хотие найти в справочнике - ')

if req.capitalize() in listName:
    index = listName.index(req.capitalize())
    phone_number=listNumber[index]
    print( f"{req.capitalize()} ", end='')
    print( phone_number)
else: print( 'Такого имени нет справочнике')

# # 2 метод запись списка в файлы и чтение из файла при поиске

# col=int(input('Вы создаете справочник. Задайте количество людей в справочнике'))

# with open('name.txt','w') as name:
#     with open('number.txt','w') as num:
#         for i in range(col):
#             tempName=input ('Имя ')
#             name.write(tempName+ '\n')
#             tempNumber=input ('Namber ')
#             num.write(tempNumber+ '\n')
        
# with open('name.txt','r') as name: 
#     listName=name.readlines()
#     listName=[name.rstrip() for name in listName]   # чтобы при считывании строк из файла не печатался символ \n окончания строки с каждым элементом
# with open('number.txt','r') as num:    
#     listNumber=num.readlines()      
            
# for i in range(col):
#     print( f"{listName[i]} ", end='')
#     print( listNumber[i])

# req=input('Введите имя, чей номер хотие найти в справочнике')

# if req in listName:
#     index = listName.index(req)
#     phone_number=listNumber[index]
#     with open('output.txt','w') as quest:
#         quest.write(f"{req}  {phone_number}" )
    