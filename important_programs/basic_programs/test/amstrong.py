n = 154
sum = 0
length_no = len(str(n))
a = n
while n!=0:
    last_digit = n%10
    sum = sum+(last_digit**length_no)
    n = n//10
if sum == a:
    print("a")
else:
    print("b")