"""
You are given an integer input N and you have to find whether it is Anshuman’s favourite or not.
If it is then print “YES” else print “NO”.
A number is Anshuman’s favourite if it is either the sum or the difference of the integer 5. (5+5, 5+5+5, 5-5,5-5-5+5+5…..)

Input:
The first line of input contains an integer denoting the number of test cases . Next line of input contains an integer N to be tested.   """

# type_input = int(input("Enter how much input: "))
# for i in range(0,type_input):
#     num = int(input("Enter the number: "))
#     if num>0:
#         result = 0
#         while result<num:
#             result = result+5
#         if result == num:
#             print("Yes")
#         else:
#             print("No")
#     elif num<0:
#         result = 0
#         while num<result:
#             result = result-5
#         if result == num:
#             print("Yes")
#         else:
#             print("No")

t = int(input())

while t>0:
    num = int(input())
    print("YES" if (num%5==0) else "NO")
    break
