from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def is_empty(self):
        return len(self.q) == 0

    def display(self):
        if self.is_empty():
            print("Q is empty")
            return
        print(self.q)
        return

    def size(self):
        print("Size : ", len(self.q))
        return

    def enque(self, new_data):
        self.q.append(new_data)
        return

    def deque(self):
        if self.is_empty():
            print("Q is empty")
            return
        popped_item = self.q.popleft()
        print("Popped : ", popped_item)
        return


myQ = Queue()
myQ.enque(1)
myQ.enque(2)
myQ.enque(3)
myQ.enque(4)
myQ.enque(5)
myQ.display()
print("Popping 1 ")
myQ.deque()
myQ.display()

myQ.size()