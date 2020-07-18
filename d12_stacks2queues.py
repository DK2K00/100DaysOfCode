class queue2():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, num):
        self.stack1.append(num)

    def dequeue(self):
        if(len(self.stack1) == 0):
            return False
        
        i = 0
        length = len(self.stack1)

        while(not self.stack1[0]):
           
            elt = self.stack1.pop()
            print(elt)
            self.stack2.append(elt)

        return_elt = self.stack1.pop()

        length = len(self.stack1)

        for i in self.stack2:

            elt = self.stack2.pop()
            self.stack1.append(elt)

        return return_elt

q = queue2()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.dequeue()
q.dequeue()

q.dequeue()