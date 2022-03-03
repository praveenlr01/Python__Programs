a="hello my #name is #praveen #whatsapp in india #facebook"
b=a.split()
print(a)
for i in b:
    if i[0]==("#"):
        print(i)
    else:
        continue
