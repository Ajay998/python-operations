# A logarithm is the inverse of an exponent.
# import math
# print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# # Logarithm base 2 of 16 is: 4.0

# We want to be able to give our influencers a simple "influencer score". It will be a small number, like less than 100. This will make it easier to "rank" them against each other in terms of how many people they are "influencing".
# Complete the get_influencer_score function. The formula for an influencer score is:
# average_engagement_percentage * log2(num_followers)

import math
def get_influencer_score(num_followers, average_engagement_percentage):
    ur_influencer_score = average_engagement_percentage * math.log(num_followers, 2)
    return ur_influencer_score
def test(num_followers, average_engagement_percentage):
    influencer_score = round(
        get_influencer_score(num_followers, average_engagement_percentage)
    )
    print(f"- num_followers: {num_followers}")
    print(f"- average_engagement_percentage: {average_engagement_percentage}")
    print(f"Influencer score: {influencer_score}")
    print("====================================")
def main():
    test(40000, 0.3)
    test(43000, 0.1)
    test(100000, 0.6)
    test(200, 0.8)
main()
