#Class to create a vertex
class Vertex():
    def __init__(self, key):
        self.id = key
        self.connections = {}

    #To create connection with another vertex
    def addNeighbour(self, nbr, weight = 0):
        self.connections[nbr] = weight

    #To return the vertex connection
    def __str__(self):
        return str(self.id) + " is connected to " + [x.id for x in self.connections]

    #To get id of vertex
    def getId(self):
        return self.id

    #To get the connections of this vertex
    def getNeighbours(self):
        return self.connections.keys()

    #To get the weight of a particular connection
    def getWeight(self, nbr):
        return self.connections[nbr]

#Class to create a graph
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    #To create a new vertex
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = newVertex
        return newVertex

    #To get a particular vertex in the graph
    def getVertex(self,n):
        if vert in self.vertList:
            return self.vertList[vert]
        
        else:
            return None

    #To check if a vertex is present in the graph
    def __contains__(self,n):
        return n in self.vertList

    #To create a connection between two vertices
    def addEdge(self,first,second,cost = 0):
        if first not in self.vertList:
            temp = self.addVertex(first)
        
        if second not in self.vertList:
            temp = self.addVertex(second)

        self.vertList[first].addNeighbour(self.vertList[second],cost)

    #To get all the vertices in the graph
    def getVertices(self):
        return self.vertList.keys()

    #To iterate through the values of the graph
    def __iter__(self):
        return iter(self.vertList.values())

#Testing
g = Graph()
for i in range(10):
    g.addVertex(i)

g.vertList

