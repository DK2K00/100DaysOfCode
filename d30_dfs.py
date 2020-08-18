#Graph example
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#Function to perform dfs
def dfs(graph, start):
    visited, stack = set(), [start]

    while(stack):
        vertex = stack.pop()

        if(vertex not in visited):
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        
    return visited

#Testing
dfs(graph, 'A')