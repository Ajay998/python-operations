a = 0
b = 1
n = 9
if n == 0:
    print(0)
if n == 1:
    print(1)
if n<0:
    print("None")
if n>1:
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    print(b)