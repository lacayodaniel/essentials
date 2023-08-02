class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, obj):
        self.data.append(obj)
        self.size += 1

    def peek(self):
        return self.data[-1]

    def pop(self):
        obj = self.peek()
        self.data.remove(obj)
        self.size -= 1
        return obj

    def clear(self):
        self.data.clear()
        self.size = 0

    def __str__(self):
        return "{}".format(self.data)

stack = Stack()
for i in range(10):
    stack.insert(i)
print(stack)
print(stack.size)
stack.clear()
print(stack)
print(stack.size)

