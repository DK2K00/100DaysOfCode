#Binary tree class
class binaryTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, new_node):
        if(self.leftChild == None):
            self.leftChild = binaryTree(new_node)
        
        else:
            t = self.leftChild
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, new_node):
        if(self.rightChild == None):
            self.rightChild = binaryTree(new_node)
        
        else:
            t = self.rightChild
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRoot(self):
        return self.key

    def setRoot(self, value):
        self.key = value

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    #Function for preorder traversal
    #root --> left --> right
    def preorder(self):
        print(self.key)
        
        if(self.leftChild):
            print(self.leftChild.preorder())

        if(self.rightChild):
            print(self.rightChild.preorder())

    #Function for postorder traversal
    #left --> right --> root
    def postorder(self):
        if(self.leftChild):
            print(self.leftChild.preorder())

        if(self.rightChild):
            print(self.rightChild.preorder())

        print(self.key)

    #Function for inorder traversal
    #left --> root --> right
    def inorder(self):
        if(self.leftChild):
            print(self.leftChild.preorder())

        print(self.key)

        if(self.rightChild):
            print(self.rightChild.preorder())

#Testing
r = binaryTree('a')
print(r.getRoot())
print(r.getLeftChild())
r.insertLeftChild('b')
print(r.getLeftChild())
print(r.getLeftChild().getRoot())
r.insertRightChild('c')
print(r.getRightChild())
print(r.getRightChild().getRoot())
r.getRightChild().setRoot('hello')
print(r.getRightChild().getRoot())

#Calling traversal functions
r.preorder()
r.inorder()
r.postorder()