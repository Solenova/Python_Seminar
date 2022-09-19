# ;  Вычислить число Пи c заданной точностью d

# ;  Пример:
# ;  - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
num=float(input('введите точность числа Пи в формате 0.001 до 10 знаков после запятой '))
result=int(math.pi/num)
col=0
while result!=0:
    col+=1
    result//=10    
 
print ('число Пи = ',int(math.pi/num)*(10**(-(col-1))))
