class Queue:

    items = []

    def __int__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        len(self.items)


if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(120)

    print(queue.dequeue())
