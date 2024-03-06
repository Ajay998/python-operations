"""
Find total number of Squares in a N*N cheesboard.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N that is the side of the chessboard.

Output:
Each seperate line showing the maximum number of squares possible.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

##############
2
2*2
1*1

4+1 = 5
##############

Example:
Input:
2
1
2

Output:
1
5
"""

N = int(input("Enter the number"))
while N>0:
    square = int(input("Enter squares: "))
    sum = 0
    while square>0:
        sum = sum+(square*square)
        square = square-1
    print(sum)
    break
