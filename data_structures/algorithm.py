# An algorithm is a fancy word that essentially means "good instructions". Here's an example of a simple algorithm that explains how to find the smallest number in a list.

# an algorithm is a finite sequence of well-defined, computer-implementable instructions. Algorithms are always unambiguous and are used as specifications for real world implementations
# Algorithms must have a/an finite_ number of steps
# Defined: there are a specific sequence of steps that performs a task
# Algorithms are always unambiguous and are used as specifications for real world implementations.
# "Algorithm" seems like a big scary word, but it really just means "well-written instructions"

# ALGORITHM - FIND MIN
# Set min to positive infinity: float("inf").
# For each number in the list nums, compare it to min. If num is smaller, set min to num.
# min is now set to the smallest number in the list.

# def find_min(nums):
#     min = float("inf")
#     for num in nums:
#         if num < min:
#             min = num
#     return min
# def test(nums):
#     res = find_min(nums)
#     print(f"Follower counts: {nums}")
#     print(f"Lowest follower count: {res}")
#     print("----")
# def main():
#     test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
#     test([12, 12, 12])
#     test([10, 200, 3000, 5000, 4])
#
# main()

# take a look at the following algorithm for adding two numbers. It might be the simplest algorithm I can think of:
# Start with input variables "a" and "b"
# Add "a" and "b" using the + operator, and assign the result to a new variable, "sum"
# Return the "sum" variable

# def sum(nums):
#     sm = 0
#     for num in nums:
#         sm = sm+num
#     return sm
#
# def test(nums):
#     res = sum(nums)
#     print(f"Follower counts: {nums}")
#     print(f"Total follower count: {res}")
#     print("----")
#
# def main():
#     test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
#     test([12, 12, 12])
#     test([10, 200, 3000, 5000, 4])
#
# main()


# How to find average: sum of list divided by number of list
