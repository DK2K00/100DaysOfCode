#Creating node class
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

#Function to traverse through list
def cycle_checker(node):

    #Assigning head node
    head = node
    next_node = node.next
    while(1):

        #Checking if node again points to head node
        if(next_node == head):
            print("List is circular")
            return True

        #If None is reached, it denotes end of linked list
        if(next_node.next == None):
            print("List is not circular")
            return False

        #Iteraing to next node
        next_node = next_node.next

#Creating actual nodes
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

#Testing
cycle_checker(a)