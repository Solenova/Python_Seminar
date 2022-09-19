# colors=['red', 'green','blue']
# data = open("file.txt", "w") # r- чтение файла, a - дозапись, w - открыть для записи(перезапишет, если там уже есть данные)
# data.writelines(colors)   # разделителей не будет
# data.close # закрываем файл

# with open("file.txt", "a") as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# path='file.txt'             #создадим путь
# data=open(path, 'r')        #откроем в режиме чтения
# for line in data:           # "прбежимся" по файлу и считаем все строки
#     print(line)
# data.close()    


# def function_name(x):
#     #body line 1
#     # ....
#     # body line n
#     # optional return


# import hello
# print(hello.f(1))

#можно использовать альяс (псевдоним) для файла
import hello as h
print (h.f(1))

list1=[22,25,6,14,3]
list2=list1

for e in list1:
    print(e)