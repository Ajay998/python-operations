# 1*1*1 + 5*5*5 + 3*3*3 = 153

num = 153
keep_num_fixed = num
sum = 0
length_of_number = len(str(num))
while num != 0:
    last_digit = num%10
    sum = sum+(last_digit**length_of_number)
    num = num//10
if sum == keep_num_fixed:
    print("Amstrong number")
else:
    print("Not")
