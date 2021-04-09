class Stack:
    def __init__(self, max_length=10):
        self.stack = [None] * max_length
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.stack)

    def push(self, new_item):
        if self.is_full():
            print("Overflow : Stack is full.")
            return
        self.stack[self.count] = new_item
        self.count += 1
        return

    def pop(self):
        if self.is_empty():
            print("Underflow : Stack is empty.")
            return
        print(self.stack)
        print(self.count)
        popped_item = self.stack[self.count - 1]
        self.stack[self.count - 1] = None
        self.count -= 1
        return popped_item

    def size(self):
        return self.count

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack[self.count - 1]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print(self.stack)
        return


myStack = Stack()
# myStack.display()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(7)
myStack.push(8)
myStack.push(9)
myStack.push(10)
myStack.display()

print("Popped item ", myStack.pop())
print("Size of stack is ", myStack.size())
myStack.display()

myStack.push(10)
print("Size of stack is ", myStack.size())
myStack.display()

myStack.push(10)
print("Size of stack is ", myStack.size())
myStack.display()

print(f"Peek : {myStack.peek()}")

print(f"Stack length : {myStack.size()}")