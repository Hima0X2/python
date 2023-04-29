Matrix=[]
R=int(input("Enter the number of rows"))
C=int(input("Enter the number of columns"))
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    Matrix.append(a)
for i in range(R):
    for j in range(C):
        print(Matrix[i][j],end=" ")
    print()