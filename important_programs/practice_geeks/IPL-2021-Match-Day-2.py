"""
Problem Link: https://practice.geeksforgeeks.org/problems/deee0e8cf9910e7219f663c18d6d640ea0b87f87/1

Due to the rise of covid-19 cases in India, this year BCCI decided to organize knock-out matches in IPL rather than a league.
Today is matchday 2 and it is between the most loved team Chennai Super Kings and the most underrated team -
Punjab Kings. Stephen Fleming, the head coach of CSK, analyzing the batting stats of Punjab. He has stats of runs scored
by all N players in the previous season and he wants to find the maximum score for each and every contiguous sub-list of
size K to strategize for the game.

Example 1:
Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output:
3 3 4 5 5 5 6
Explanation:
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6


Your Task:
You don't need to read input or print anything. Complete the function max_of_subarrays() which takes the array, N,
and K as input parameters and returns a list of integers denoting the maximum of every contiguous subarray of size K.

Constraints:
1 ≤ N ≤ 106
1 ≤ K ≤ N
0 ≤ arr[i] ≤ 106
"""

arr = [8 ,5 ,10 ,7 ,9 ,4 ,15 ,12 ,90 ,13]
n = len(arr)
k = 4
for i in range(0,n):
    if i+k<=n:
        a_list = []
        for j in range(i,i+k):
            a_list.append(arr[j])
        print(a_list,"-->",max(a_list))



