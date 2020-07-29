#Class to create node
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#Method to get maximum value of a subtree
def treemax(node):
    if not node:
        return float("-inf")
        
    else:
        maxleft = treemax(node.left)
        maxright = treemax(node.right)
        return max(node.key, maxleft, maxright)

#Method to get minimum value of a subtree
def treemin(node):
    if not node:
        return float("inf")

    else:
        minleft = treemin(node.left)
        minright = treemin(node.right)
        return min(node.key, minleft, minright)

#Method to check whether binary tree is a bst
def validate(node):
    if not node:
        return True

    if(treemax(node.left) <= node.key <= treemin(node.right) and validate(node.left) and validate(node.right)):
        return True

    else:
        return False

#Testing
root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(validate(root))

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(validate(root))
