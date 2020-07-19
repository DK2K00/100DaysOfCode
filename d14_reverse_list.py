#Creating class Node
class node():
    def __init__(self, value):
        self.value = value
        self.next = None

#Creating reverse function
def reverse(head):
    current = head
    next_node = None
    previous = None

    #Traversing list
    while(current):

        #Pointing to next nodes
        next_node = current.next
        current.next = previous

        #Switching nodes
        previous = current
        current = next_node

    return previous

#Creating nodes
a = node(10)
b = node(20)
c = node(30)
d = node(40)

a.next = b
b.next = c
c.next = d

reverse(a)

#Testing
print(a.next)
print(d.next.value)