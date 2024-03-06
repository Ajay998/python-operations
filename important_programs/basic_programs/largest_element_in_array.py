a = [1,25,3,4]
print(max(a))

largest = a[0]
for i in range(1,len(a)):
    if a[i]>largest:
        largest = a[i]

print(largest)