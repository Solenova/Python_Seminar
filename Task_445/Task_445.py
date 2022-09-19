# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
f = open('polinom1.txt', 'r')
numbers1 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers1.insert(0, i)
print(numbers1)

f = open('polinom2.txt', 'r')
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









# import itertools

# def addPoly(*args):
#     expval = sorted([(e, v) for poly in args for v, e in poly])
#     return [
#         (sum(v for _, v in g), e)
#         for e, g in itertools.groupby(expval, key=lambda kv: kv[0])
#     ]

# print(addPoly([(4,3),(8,1),(3,0),(8,9)],[(4,3),(2,1), (8,7),(6,0),(23,31)]))











# import re
# import itertools


# file1 = 'polinom1.txt'
# file2 = 'polinom2.txt'
# file_sum = 'Sum_polynom.txt'

# # Получение данных из файла

# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# # Получение списка кортежей каждого (<коэффициент>, <степень>)

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# # Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# # Составление итогового многочлена

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)





















# import re
# import itertools
# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# polinom1=read_pol('polinom1.txt')
# print(polinom1)
# polinom2=read_pol('polinom2.txt')
# print(polinom2)

# Получение списка кортежей каждого (<коэффициент>, <степень>)

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# poly1=convert_pol(polinom1)
# print(poly1)
# poly2=convert_pol(polinom2)
# print(poly2)











# import regex

#  s = 'P = 3x^2 + 2x + 7'.replace(' ', '')
#  poly = []
#  for term in regex.findall(r'[+-]?\d*\w+\^?\d*', s):
#      term = regex.sub(r'(\d*)([A-Za-z]\w*)(.*)', r'\1*\2\3', term)
#      term = term.replace('^', '**')
#      poly.append(term)
 
#  poly=['*P', '3*x**2', '+2*x', '+7']
#  poly[0]=poly[0][1:]+'='
#  poly = ''.join(poly)
#  poly='P=3*x**2+2*x+7'
#  from sympy import *
#  P =sympify(poly[2:])
#  P
# # 3*x**2 + 2*x +7