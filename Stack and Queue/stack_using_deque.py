from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, new_ele):
        self.stack.append(new_ele)
        return

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        popped_ele = self.stack.pop()
        print("Popped ele : ", popped_ele)
        return

    def seek(self):
        print("Seek : ", self.stack[-1])
        return

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack : ", self.stack)
        return


myStack = Stack()
myStack.push(50)
myStack.push(40)
myStack.push(30)
myStack.push(20)
myStack.push(10)
myStack.display()
myStack.pop()
myStack.display()
myStack.seek()
myStack.display()
