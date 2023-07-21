class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


print(' *** Stack implement by Python list***')

data = input('Enter data to stack : ').split()
s = Stack()

for e in data:
    s.push(e)

print(f'{s.size()} Data in stack :  {s.items}')

while not s.isEmpty():
    s.pop()

print(f'{s.size()} Data in stack :  {s.items}')