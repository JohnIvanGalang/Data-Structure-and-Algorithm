class Stacks:
    def __init__(self):
        self.items = []
        self.max_size = 10

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def is_Empty(self):
        return len(self.items) != 0

    def is_Full(self):
        return self.max_size is not None and len(self.items) == self.max_size

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


stack = Stacks()

stack.display()
stack.is_Full()
stack.push(9)
stack.push(4)
stack.is_Empty()
stack.size()
stack.peak()
stack.push(6)
stack.size()
stack.pop()
stack.display()
