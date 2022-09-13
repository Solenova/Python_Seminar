# В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить количество в ней символов и слов.
f=open("text.txt","r")
count=0
listStr=[]  # список с количествами симовлов в строках
for line in f:
    count=0
    summStr=len(line)               #количество  строк
    listStr.append(summStr)         #количество символов в каждой строке (добавлены в список)
    for i in range(len(line)):      
        if line[i]==" " or line[i]=="\n": count+=1
        # print(line[i])
    print(f'количество слов в строке',count)
print (f'количество строк',len(listStr))
print (f'количество символов в строках',listStr)   
f.close()

