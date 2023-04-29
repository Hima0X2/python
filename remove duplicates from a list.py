n=input("")
list=n.split()
d=set()
e=[]
for x in list:
    e.append(x)
    d.add(x)
# d.sort()
print(sorted(d)[-2])