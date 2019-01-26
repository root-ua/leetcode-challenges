class Stack:

    def __int__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(5)
    stack.push(101)

    stack.pop()
