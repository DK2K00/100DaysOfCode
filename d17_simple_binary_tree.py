#Function to create simple binary tree
def binaryTree(r):
    return [r, [], []]

#To create left child
def insertLeft(root, newBranch):
    t = root.pop(1)

    if(len(t) > 1):
        root.insert(1, [newBranch, t, []])

    else:
        root.insert(1, [newBranch, [], []])

    return root

#To create right child
def insertRight(root, newBranch):
    t = root.pop(2)

    if(len(t) > 1):
        root.insert(2, [newBranch, [], t])

    else:
        root.insert(2, [newBranch, [], []])

    return root

#To return root
def getRoot(root):
    return root[0]

#To create or change root value
def newRoot(root, val):
    root[0] = val

#To return left child
def getLeftChild(root):
    return root[1]

#TO return right child
def getRightChild(root):
    return root[2]

#Testing
b = binaryTree(5)
insertLeft(b, 4)
insertLeft(b, 7)
insertRight(b, 6)
getRoot(b)
newRoot(b, 1)
getLeftChild(b)
getRightChild(b)