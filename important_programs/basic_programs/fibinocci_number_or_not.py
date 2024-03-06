# 5n^2+4 or 5n^2-4 = perfect squarwe
import math
for i in range(1,11):
    condition1 = (5*i*i+4)
    condition2 = (5*i*i-4)
    sqrt_cond1 = int(math.sqrt(condition1))
    sqrt_cond2 = int(math.sqrt(condition2))
    if sqrt_cond1*sqrt_cond1 == condition1:
        print(i, "is a Fibonacci Number")
    elif sqrt_cond2*sqrt_cond2 == condition2:
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is not Fibonacci Number")