class Graph:
    def __init__(self):
            self.adjList=dict() #hashmap

    def addVertex(self,vertex):
            self.adjList[vertex]=list()

    def addEdge(self,vertex1,vertex2):
            self.adjList[vertex1].append(vertex2)

    def getNeighbors(self,vertex):
            return self.adjList.get(vertex,None)
        
def dfs(graph,start):
    visited=set()
    def dfs(node,visited):
        if node in visited:
            return
        print(node)
        visited.add(node)
        neighbors=graph.getNeighbors(node)
        for neighbor in neighbors:
            dfs(neighbor,visited)
    dfs(start,visited)
    
graph=Graph()
vertices=['E', 'D', 'W', 'A', 'R']

for vertex in vertices:
	graph.addVertex(vertex)

graph.addEdge('E','D')
graph.addEdge('D','W')
graph.addEdge('A','R')
graph.addEdge('R','D')
#print(graph.adjList) #testing

print("DFS Traversal starting from vertex E:")
dfs(graph,'E')