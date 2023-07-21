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

    def peek(self):
        return self.items[-1]


def infix2postfix(expression):
    priority = '^', '$', '*/', '+-', '><=#', '.', '|'
    order = lambda char: [i for i, p in enumerate(priority) if char in p][0]
    stack = Stack()
    l = ''

    for char in expression:
        
        if char in ''.join(priority):            
            while not stack.isEmpty() and (
                stack.peek() != '(' and 
                order(char) >= order(stack.peek())
            ):
                l += stack.pop()
                
            stack.push(char)
                
        elif char == '(':
            stack.push(char)
            
        elif char == ')':
            while stack.peek() != '(':
                l += stack.pop()
                         
            stack.pop()
            
        else: 
            l += char

    while not stack.isEmpty():
        l += stack.pop()
        
    return l


print(' ***Infix to Postfix***')
expression = input('Enter Infix expression : ')
print('PostFix :')
print(infix2postfix(expression))