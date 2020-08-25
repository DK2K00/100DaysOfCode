#Class to create tree node
class TreeNode:
    #Constructor
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    #Checking to see if there's a left child
    def hasLeftChild(self):
        return self.leftChild

    #Checking to see if there's a right child
    def hasRightChild(self):
        return self.rightChild

    #Checking to see if it is the left child
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    #Checking to see if it is the right child
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    #Checking to see if node is a root node
    def isRoot(self):
        return not self.parent

    #Checking to see if node is a leaf node
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    #Checking to see if node has any leaf nodes
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    #Checking to see if node has both leaf nodes
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    #Function to replace node data
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


#Class to create a binary tree
class BinarySearchTree:
    #Constructor
    def __init__(self):
        self.root = None
        self.size = 0

    #Length of tree
    def length(self):
        return self.size

    #Helper function for length function
    def __len__(self):
        return self.size

    #To insert a new node into the tree
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    #Private function for inserting node
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    #Used to insert elements using dictionaries
    def __setitem__(self,k,v):
        self.put(k,v)

    #To search data from a tree and retrieve it
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                
                return res.payload
            else:
                return None
        else:
            return None

    #Private function
    def _get(self,key,currentNode):       
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    #To delete a node from the tree
    def delete(self,key):       
        if self.size > 1:
            
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):       
        self.delete(key)

    #Function to splice the nodes
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                
                if self.isLeftChild():
                    
                    self.parent.leftChild = self.leftChild
                else:
                    
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
        else:
                    
            if self.isLeftChild():
                        
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    #Function to find successor node after deletion
    def findSuccessor(self):  
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                
                if self.isLeftChild():
                    
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    #To find the minimum value in a tree
    def findMin(self):    
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    #Function to actually remove the node
    def remove(self,currentNode): 
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

#Testing
mytree = BinarySearchTree()

mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[4])
print(mytree[3])