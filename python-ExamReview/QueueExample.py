
class Queue: # FIFO
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0

    def enqueue(self, item):
        self.items.insert(0, item) # will always append to the beginning

    def dequeue(self):
        self.items.remove(self.items[-1]) # remove takes an element, items[0] returns the first element

    def size(self):
        return len(self.items)

    def __str__(self):
        return "{}".format(self.items)

