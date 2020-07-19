#Creating node class
class node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#Creating actual nodes with values
a = node(10)
b = node(20)
c = node(30)
d = node(40)

#Creating the doubly linked list list
a.next = b

b.prev = a
b.next = c

c.prev = b
c.next = d

d.prev = c

#Testing
print(a.value)
print(a.next.value)
print(d.prev.value)
print (d.value)

#Now modifying the doubly linked list to circular linked list
a.prev = d
d.next = a

#Testing
print(a.prev.value)
print(d.next.value)