class Deque:
    def __init__(self):
        self.deque = []

    def size(self):
        print("Size: ", len(self.deque))
        return

    def is_empty(self):
        return len(self.deque) == 0

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return
        print("Length: ", len(self.deque))
        return

    def add_left(self, new_ele):
        self.deque.insert(0, new_ele)

    def add_right(self, new_ele):
        self.deque.append(new_ele)
        return

    def remove_left(self, new_ele):
        if self.is_empty():
            print("Nothing to delete")
            return

    def remove_right(self, new_ele):
        if self.is_empty():
            print("Nothing to delete")
            return
        print("Popped ele: ", self.deque.pop())
        return
