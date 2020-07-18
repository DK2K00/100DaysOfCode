class node():

    def __init__(self, value):
        self.value = value
        self.next = None

a = node(10)
b = node(20)
c = node(30)

a.next = b
b.next = c

print(a.value)
print(a.next.value)
print(c.next)
