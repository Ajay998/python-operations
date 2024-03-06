# Given two positive integers num1 and num2, the task is to find the sum of the two numbers on a
# 12 hour clock rather than a number line.
t1 = 5
t2 = 3
time = t1+t2
if time<12:
    print(time)
else:
    print(time%12)