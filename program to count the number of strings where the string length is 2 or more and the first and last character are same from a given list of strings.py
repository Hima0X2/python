n=input()
list=n.split()
count=0
for x in list:
    l=len(x)
    if(x[0]==x[-1]) and l>=2:
        count=count+1
print("count",count)
