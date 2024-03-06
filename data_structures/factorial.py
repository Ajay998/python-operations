# In math, the factorial of a positive integer n, written n!, is the product of all positive integers less than and equal to n
# 5! = 5 * 4 * 3 * 2 * 1
def num_possible_orders(num_posts):
    fact = 1
    for i in range(1,num_posts+1):
        fact = fact*i
    return fact
def test(num_posts):
    orders = num_possible_orders(num_posts)
    print(f"- num_posts: {num_posts}")
    print(f"Possible orders: {orders}")
    print("====================================")
def main():
    test(2)
    test(3)
    test(5)
    test(7)
    test(9)
    test(11)
main()