# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
List[pos1-1],List[pos2-1] = List[pos2-1],List[pos1-1]
print(List)