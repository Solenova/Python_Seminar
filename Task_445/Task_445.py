# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

def add(p1,p2):
    x = [0]*(max(p1[0][1],p2[0][1])+1)
    for i in p1+p2:
        x[i[1]]+=i[0]
    res =  [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mul(p1,p2):
    x = [0]*(p1[0][1]*p2[0][1]+1)
    for i in p1:
        for j in p2:
            x[i[1]+j[1]]+=i[0]*j[0]
    res = [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res
def poly_add( x, y):
  r = []
  min_len = min( len(x), len(y))
  for i in range(min_len):
    if x[i][1] == y[i][1]:
      m = x[i][0] + y[i][0]
      if m != 0:
        r.append((m, x[i][1])) 
    if x[i][1] != y[i][1]:
      r.append((y[i]))
      r.append((x[i]))
  return r

res=add([(4,3),(3,0)],[(-4,3),(2,1)])
print(res)