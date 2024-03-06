k = 2
n = 3
a = 0
b = 1
i = 2
while i!=0:
    c = a+b
    a = b
    b = c
    if c%k == 0:
        print(n*i)
        break
    i = i+1