a=input("Enter the string: ")
b=a.split()
c=[]
for i in b:
    if len(i)%2==0:
        c.append(i)
    else:
        i=i[::-1]
        c.append(i)
        
print("a = ",a)
c=" ".join(c)
print("result = ",c)
