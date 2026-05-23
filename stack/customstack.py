class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        
    def is_empty(self):
        return (len(self.stack) == 0)    

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def print_stack(self):
        if self.is_empty():
            print("Stack is Empty!")
            return
        for i in range(self.size() - 1, -1, -1):
            display_item = str(self.stack[i])
            print(f"|{display_item}|")


mystack = Stack()
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.push(8)
mystack.print_stack()


# Task: Reverse this string using custom stack:
mystring = "hello"

a = Stack()
for i in mystring:
    a.push(i)
s = ""    
while not a.is_empty():
    s += a.pop()
print(s)