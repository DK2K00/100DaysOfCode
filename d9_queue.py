class queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()

    def length(self):
        return len(self.items)

    def IsEmpty(self):
        return self.items == []


q = queue()
q.IsEmpty()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.length()
q.dequeue()
q.dequeue()
q.IsEmpty()
q.dequeue()
q.IsEmpty()