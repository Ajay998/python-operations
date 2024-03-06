# Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
# Output: 3
# weight = 4
# weight should be less than 4 need to get maximum profit

# profit[] = {1, 2, 3}, weight[] = {4, 5, 6} Weight = 3

import itertools
profit = [1, 2, 3]
weight = [4, 5, 1]

max_weight = 4
max_profit = 0
for j in range(0,len(weight)):
    if weight[j] > max_weight:
        continue
    else:
        profit_b = profit[j]
        if profit_b>max_profit:
            max_profit = profit_b

print(max_profit)



