f = open('file.txt', 'r')
numbers1 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers1.insert(0, i)
print(numbers1)

f = open('file1.txt', 'r')
numbers2 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers2.insert(0, i)
print(numbers2)

result = []
if len(numbers1) > len(numbers2):
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(1, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])
    for i in range(len(numbers2), len(numbers1)):
        result.insert(0, numbers1[i])
elif len(numbers1) < len(numbers2):
    for i in range(1, len(numbers1)):
        if i % 2 == 0:
            result.insert(0, numbers2[i])
        else:
            result.insert(0, numbers2[i] + numbers1[i])
    for i in range(len(numbers1), len(numbers2)):
        result.insert(0, numbers2[i])
else:
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(0, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])

print(result)

s = []
f = open('file2.txt', 'w')
for i in range(0, len(result)):
    if i % 2 == 0:
        s.append(f'{result[i]}')
    else:
        if result[i] == 1:
            s.append(f'*x+')
        else:
            s.append(f'*x^{result[i]}+')
s.append('=0')
f.writelines(s)
f.close()







# def sum_poly(a,b):
#     na=len(a)
#     nb=len(b)
#     r=[]
#     ia,ib=-1,-1
#     while abs(ia)<=na or abs(ib)<=nb:
#         c=0
#         if abs(ia)<=na:
#             c+=a[ia]
#         if abs(ib)<=nb:
#             c+=b[ib]
#         r=[c]+r 
#         ia-=1
#         ib-=1
#     i=0
#     while r[i] ==0 and i<len(r)-1:
#         i+=1
#     return r[i:]  
    
# n=int(input())
# a=list(map(int,input().split()))
# m=int(input())
# b=list(map(int,input().split()))
# r=sum_poly(a,b)
# print(len(r)-1)
# print(*r)
# 1






# class Polynomial:
#     def __init__(self, coefficients):
#         self.coefficients = coefficients
#     def __call__(self, x):
#         return sum([self.coefficients[i]*x**i for i in range(len(self.coefficients))])
#     def __add__(self, p):
#         a = self.coefficients
#         b = p.coefficients
#         if len(a)<len(b):
#              a += [0]*(len(b)-len(a))
#         else:
#             b += [0]*(len(a)-len(b))
#         return Polynomial([a[i]+b[i] for i in range(len(a))])
# a=Polynomial((4,3),(8,1))
# # ,(8,1),(3,0),(8,9)],[(4,3),(2,1), (8,7),(6,0),(23,31)])      
# print(a)  