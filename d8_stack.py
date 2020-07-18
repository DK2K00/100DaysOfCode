class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def IsEmpty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

s = Stack()
s.IsEmpty()
s.push(10)
s.length()
s.push(20)
s.push(30)

s.length()
s.peek()
s.pop()
s.IsEmpty()
s.pop()
s.pop()
s.IsEmpty()