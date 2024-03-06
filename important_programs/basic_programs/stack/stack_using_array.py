class StackArray:
    def __init__(self):
        self.data = []
    def push(self,element):
        self.data.append(element)
    def pop(self):
        if self.data == []:
            return "Empty data"
        print("Pop element: ",self.data.pop())
        return self.data
    def empty(self):
        if len(self.data) == []:
            return 0
    def top(self):
        if len(self.data) == []:
            return "Empty list"
        return self.data[-1]

array_stack = StackArray()
array_stack.push(5)
array_stack.push(7)
array_stack.push(9)
print('Push Element:', array_stack.data)
print('Pop Element data:', array_stack.pop())
print('Top Element:', array_stack.top())



