#Class for binary tree
class binaryHeap():
    def __init__(self):
        self.heaplist = [0]
        self.current_size = 0

    #Function to swap elements from bottom to top of the heap
    def percUp(self, i):
        while(i // 2 > 0):
            if(self.heaplist[i] < self.heaplist[i // 2]):

                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            
            i = i // 2

    #Function to insert elements into the binary heap
    def insert(self, k):
        self.heaplist.append(k)
        self.current_size += 1
        self.percUp(self.current_size)

    #Function to swap elements from top to bottom of the heap
    def percDown(self, i):
        while(i * 2 <= self.current_size):
            mc = self.minChild(i)

            if(self.heaplist[i] > self.heaplist[mc]):
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = temp

            i = mc

    #To find the minimum element based on index given
    def minChild(self, i):
        if((i * 2) + 1 > self.current_size):
            return i * 2

        else:
            if(self.heaplist[i * 2] < self.heaplist[(i*2) + 1]):
                return i * 2

            else:
                return (i*2) + 1

    #To remove the minimum element in the binary heap
    def delMin(self):
        val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.current_size]
        self.current_size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return val

    #To build a binary heap by inputting a list of elements
    def buildHeap(self, lst):
        i = len(lst) // 2
        self.current_size = len(lst)
        self.heaplist = [0] + lst[:]
        while(i > 0):
            self.percDown(1)
            i = i - 1

#Testing
b = binaryHeap()
b.buildHeap([5,2,1,3,4])  
b.insert(7)
b.minChild(2)
b.delMin()