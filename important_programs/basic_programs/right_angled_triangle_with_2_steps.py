num = int(input("Enter the rows: "))
k = 1
for i in range(0,num):
    for j in range(1,k+1):
        print("*",end=" ")
    k = k+2
    print()