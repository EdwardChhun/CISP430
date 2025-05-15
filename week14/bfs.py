class Graph:
    def __init__(self):
            self.adjList=dict() #hashmap

    def addVertex(self,vertex):
            self.adjList[vertex]=list()

    def addEdge(self,vertex1,vertex2):
            self.adjList[vertex1].append(vertex2)

    def getNeighbors(self,vertex):
            return self.adjList.get(vertex,None)
        
def bfs(graph,start):
    visited=set()
    queue=[start]
    visited.add(start)
    while (len(queue)>0):
        vertex=queue.pop(0) #pop from the front
        print(vertex)
        neighbors=graph.getNeighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
graph=Graph()
vertices=['E', 'D', 'W', 'A', 'R']

for vertex in vertices:
	graph.addVertex(vertex)

graph.addEdge('E','D')
graph.addEdge('D','W')
graph.addEdge('A','R')
graph.addEdge('R','D')
#print(graph.adjList) #testing

print("BFS Traversal starting from vertex E:")
bfs(graph,'E')