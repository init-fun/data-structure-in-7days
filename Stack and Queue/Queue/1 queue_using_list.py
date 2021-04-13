class Queue:
    def __init__(self, max_length=5):
        self.q = [None] * max_length
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.front == self.count

    def is_full(self):
        return self.count == len(self.q)

    def size(self):
        return len(self.q) - self.front

    def enque(self, new_data):
        if self.is_full():
            print("Overflow: Q is full")
            return
        self.q[self.count] = new_data
        self.count += 1
        return

    def deque(self):
        if self.is_empty():
            print("Undeflow: Q is empty")
            return

        poppedn_item = self.q[self.front]
        self.q[self.front] = None
        self.front += 1
        return poppedn_item

    def peek(self):
        if self.is_empty():
            print("Q is empty")
            return
        return self.q[self.front]

    def display(self):
        print(self.q)
        return


myQ = Queue()
myQ.enque(1)
myQ.enque(2)
myQ.enque(3)
myQ.enque(4)
myQ.enque(5)
myQ.display()
print(myQ.is_full())
# myQ.enque(5)
print("Popping 1 ")
myQ.deque()
myQ.display()

print(myQ.size())
print(myQ.peek())