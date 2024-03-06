list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10, 85]
N = 2
list2 = []
largest = list1[0]
for i in range(0,len(list1)):
    if list1[i]>largest:
        largest = list1[i]
print(largest)

second_largest = list1[0]
for j in range(0,len(list1)):
    if list1[j]>second_largest:
        if list1[j]!=largest:
            second_largest = list1[j]
print(second_largest)
list2.append(second_largest)
list2.append(largest)
print(list2)
