"""
    Stack Data Structure
    Pop - Removes the first element on top of the stack
    Push add an element to the stack eg : Push(value)
    get_stack - Returns all elements in the stack
    Peek - Returns the element on top of the stack
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# Implementation
# myStack = Stack()
# myStack.push("A")
# myStack.push("B")
# myStack.push("C")
# print( myStack.get_stack() )
# myStack.pop()
# print(myStack.pop())
# # print(myStack.peek())
# print( myStack.get_stack() )
