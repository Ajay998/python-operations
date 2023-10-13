# An exponent indicates how many times a number is to be multiplied by itself.
# For example: 53 = 5 * 5 * 5

# square = 2 ** 2
# # square = 4
# cube = 2 ** 3
# # cube = 8

# In the social media industry, there is a concept called "spread" - it refers to how much a post spreads due to "reshares" after all of the original author's followers see it.
# Complete the get_estimated_spread function. The only input is audiences_followers, which is a list of the follower counts of all the followers of the author.
# As it turns out, social media posts spread at an exponential rate! We've found that the estimated spread of a social post can be calculated using the following formula:
# estimated_spread = average_audience_followers * ( num_followers^1.2 )
# In the formula above, average_audience_followers refers to an average calculated from each number within the audiences_followers argument - which is a list containing the user's follower's individual follower count.
# For example, if audiences_followers = [2, 4, 2, 19], then the influencer has 4 followers, and each of them has their own follower counts of 2, 4, 2, and 19 respectively.

# def get_estimated_spread(audiences_followers):
#     sum = 0
#     for num in audiences_followers:
#         sum += num
#
#     num_followers = len(audiences_followers)
#     average_audience_followers = sum / num_followers
#     return average_audience_followers * (num_followers ** 1.2)
# def test(nums):
#     res = round(get_estimated_spread(nums))
#     print(f"Follower counts: {nums}")
#     print(f"Estimated spread: {res}")
#     print("====================================")
# def main():
#     test([7, 4, 3, 100, 765, 2344, 1, 2, 32])
#     test([12, 12, 12])
#     test([10, 200, 3000, 5000, 4])
# main()

# Complete the get_follower_prediction function.
# "fitness" influencers have their follower count quadruple each month
# "cosmetic" influencers have their follower count triple each month
# All other influencers have their follower count double each month
# For example, if a fitness influencer starts with 10 followers, then after 1 month they should have 40 followers. After 2 months, they would have 160 followers. etc.
# EXTRA CREDIT
# Try to avoid using a loop by using a slightly modified geometric sequence formula instead.
# total = a1 * r^n

# def get_follower_prediction(follower_count, influencer_type, num_months):
#     if influencer_type == "fitness":
#         total = follower_count * (4 ** num_months)
#     elif influencer_type == "cosmetic":
#         total = follower_count * (3 ** num_months)
#     else:
#         total = follower_count * (2 ** num_months)
#     return total
# def test(follower_count, influencer_type, num_months):
#     predicted = get_follower_prediction(follower_count, influencer_type, num_months)
#     print(f"- Follower count: {follower_count}")
#     print(f"- Type: {influencer_type}")
#     print(f"- Months: {num_months}")
#     print(f"Prediction: {predicted}")
#     print("====================================")
# def main():
#     test(10, "fitness", 1)
#     test(10, "fitness", 2)
#     test(10, "fitness", 4)
#     test(12, "cosmetic", 4)
#     test(15, "business", 4)
#     test(10, "fitness", 5)
#     test(10, "fitness", 6)
#     test(10, "fitness", 7)
#     test(10, "fitness", 8)
#     test(10, "fitness", 9)
# main()