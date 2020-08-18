#Importing library
from enum import Enum
from collections import OrderedDict

#Class for enumeration
class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

#Class to create a node
class Node:
    def __init__(self,num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()

    def __str__(self):
        return str(self.num)

#Class to create a graph
class Graph:
    def __init__(self):
        self.nodes = OrderedDict()
    
    def add_Node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self,source,dest,weight = 0):
        if(source not in self.nodes):
            self.add_Node(source)

        if(dest not in self.nodes):
            self.add_Node(dest)
        
        self.nodes[source].adjacent[self.nodes[dest]] = weight

#Testing
g= Graph()
g.add_edge(0,1,5)
g.add_edge(1,2,6)

g.nodes