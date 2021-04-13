from collections import deque


class Queue:
    def __init__(self, max_len=5):
        self.q = deque([None] * max_len)
        self.count = 0

    def is_full(self):
        return len([True for i in self.q if i is not None]) == self.count

    def is_empty(self):
        return len([True for i in self.q if i is not None]) == 0

    def display(self):
        if self.is_empty():
            print("Q is empty")
            return
        for i in self.q:
            if i is not None:
                print(i, end=" > ")
        return

    def size(self):
        print("Size : ", len([True for i in self.q if i is not None]))
        return

    def enque(self, new_data):
        if self.is_full():
            print("Overflow: Q is full")
            return
        self.q[self.count] = new_data
        self.count += 1
        return

    def deque(self):
        if self.is_empty():
            print("Underflow: Q is empty")
            return
        popped_item = self.q.popleft()
        self.count -= 1
        print("Popped : ", popped_item)

        return


myQ = Queue()
print(myQ.is_full())
myQ.enque(1)
myQ.enque(2)
myQ.enque(3)
myQ.enque(4)
myQ.enque(5)
print(myQ.is_full())
myQ.display()
myQ.deque()
myQ.display()

myQ.size()