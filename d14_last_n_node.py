#Creating class Node
class node():
    def __init__(self, value):
        self.value = value
        self.next = None

#Creating left and right pointer
def last_n(head, n):

    left = head
    right = head

    #Pushing right pointer to move n - 1 spaces between left and right
    for i in range(n-1):
        
        if(not right.next):
            return False

        right = right.next

    while(right.next):
        left = left.next
        right = right.next

    return left

#Creating nodes
a = node(10)
b = node(20)
c = node(30)
d = node(40)
e = node(50)

a.next = b
b.next = c
c.next = d
d.next = e

#Testing
ans = last_n(a, 2)
print(ans.value)