from collections import deque


class Stack:
    def __init__(self, max_len=10):
        self.stack = deque([None] * max_len)
        self.count = 0

    def is_empty(self):
        # return len(self.stack) == 0
        return self.count == 0 or len(self.stack) == 0

    def is_full(self):
        return self.count == len(self.stack)

    def push(self, new_ele):
        if self.is_full():
            print("Overflow : Stack is full")
            return
        self.stack[self.count] = new_ele
        self.count += 1
        return

    def pop(self):
        if self.is_empty():
            print("Underflow: Stack is empty")
            return
        popped_ele = self.stack[self.count - 1]
        self.stack[self.count - 1] = None
        self.count -= 1
        print("Popped ele : ", popped_ele)
        return

    def seek(self):
        print("Seek ", self.stack[self.count - 1])
        return

    def size(self):
        total_len = len([True for i in self.stack if i is not None])
        print("Size : ", total_len)
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

print(myStack.is_full())

myStack.size()
myStack.display()

myStack.pop()
myStack.size()

myStack.display()

myStack.seek()
myStack.display()
