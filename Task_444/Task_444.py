# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
# создание списка коэффициентов
level=int(input('введите степень многочлена (натуральное число) - '))
listCoeff=[]
for i in range(level+1):
    temp=random.randint(0,100)
    listCoeff.append(temp)
print (listCoeff)
#создание списка одночленов полинома
result=[]
i=level
while i>=0:
    if listCoeff[i]==0: result.append(0)
    elif listCoeff[i]==1: result.append(f'x^{i}')
    elif i==0:result.append(f'{listCoeff[i]}')
    elif i==1:result.append(f'{listCoeff[i]}*x')
    elif listCoeff[i]!=0 and listCoeff[i]!=1: result.append(f'{listCoeff[i]}*x^{i}')
    i-=1

#запись полинома в переменную polinom    
polinom=""
for i in result:
    
    if i==result[-1]: polinom+=f'{i}=0'
    elif i!=0: polinom+=f'{i}+'
print(polinom)

# вывод в файл
f=open("text.txt","w")
f.write(polinom)
f.close()


