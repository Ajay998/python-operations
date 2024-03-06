# What is prime number?
# Either 0 or 1 .... From 2 to the choosen before number ... The number should not be divisible

# 1) choose number
# 2) number should greater than 1
# 3) range 2 to number
# 4) if divisible ==0 break
# 5) else num


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
if start<end:
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)
