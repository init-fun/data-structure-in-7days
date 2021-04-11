class Queue:
    def __init__(self):
        self.q = []
        self.front = 0

    def is_empty(self):
        return self.front == len(self.q)

    def size(self):
        return len(self.q) - self.front

    def enque(self, new_data):
        self.q.append(new_data)
        return

    def deque(self):
        if self.is_empty():
            print("Q is empty")
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
