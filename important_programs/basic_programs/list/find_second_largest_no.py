# a = [1,2,3,3]
# list2 = list(set(a))
# list2.sort()
# print(list2[-2])


nums = []
print("Enter 10 Elements (Numbers) for List: ")
for i in range(10):
  nums.append(int(input()))

large = nums[0]
for i in range(10):
  if large<nums[i]:
    large = nums[i]

secondLarge = nums[0]
for i in range(10):
  if secondLarge<nums[i]:
    if nums[i]!=large:
      secondLarge=nums[i]

print("\nSecond Largest Number is: ")
print(secondLarge)