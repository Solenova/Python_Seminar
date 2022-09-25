# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.
# ​Пример: ​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​
listNum=[1, 2, 3, 5, 1, 5, 3, 10]
print(listNum)

def Only(data):
    unique=[]
    for i in range(len(data)):
        count=0
        for j in range(len(data)):
            if data[i]==data[j] and i!=j:
                count+=1
        if count==0: unique.append(data[i])
    return unique

print(Only(listNum))

# 2 method улучшение кода

# print(list(filter(lambda x: listNum.count(x)==1, listNum)))
