#Class to create node
class Node():
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#Method to print values based on tree level
def levelorder(tree):
    nodes = [tree]

    while(nodes):
        out = []

        for i in range(len(nodes)):
            node = nodes.pop(0)
            out.append(node.key)

            if(node.left):
                nodes.append(node.left)
            
            if(node.right):
                nodes.append(node.right)

        for item in out:
            print(item, end = " ")
        print("\n")

#Testing
root = Node(10, 1)
root.left = 2
root.right = 3

levelorder(root)