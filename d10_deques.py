class deques():
    def __init__(self):
        self.items = []

    def addFront(self,item):
        return self.items.append(item)

    def addRear(self,item):
        return self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(1)

    def length(self):
        return len(self.items)

    def IsEmpty(self):
        return self.items == []

d = deques()
d.IsEmpty()
d.addFront(10)
d.addFront(20)
d.addRear(30)
d.length()
d.removeRear()
d.removeRear()
d.IsEmpty()
d.removeFront()
d.IsEmpty()