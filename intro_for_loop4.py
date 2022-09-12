a="is2 th1is a3 t4est"
b=a.split()
c=[]
l=len(b)
n="1","2","3","4"
j=0
while j<=l-1:
    for i in range(l):
        if n[i] in b[j]:
            c.append(b[i])
            j+=1
print(a)
c=" ".join(c)
print(c)
