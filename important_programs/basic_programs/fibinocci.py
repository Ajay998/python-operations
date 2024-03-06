# Fibinocci
#  fib of 0 = 0
#  fib of 1 = 1
#  fib of less than 0 incorrect op
#  start range from 2 to num   if num=9 ==> range(2,9)
#  add c = a+b
#  swap a = b
#  swap c = b

n = 9
a = 0
b = 1
if n == 0:
    print(0)
if n == 1:
    print(1)
if n < 0:
    print("Incorrect input")
if n>1:
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    print(b)


