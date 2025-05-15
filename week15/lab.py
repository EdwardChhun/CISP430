class Graph:
    def __init__(self):
            self.adjList=dict() #hashmap

    def addVertex(self,vertex):
            self.adjList[vertex]=list()

    def addEdge(self,vertex1,vertex2):
            self.adjList[vertex1].append(vertex2)

    def getNeighbors(self,vertex):
            return self.adjList.get(vertex,None)
        
def constructPath(predecessors,end):
    node=end
    path=list() #will be in reverse order
    while node!=-1:
            path.append(node)
            node=predecessors[node]#get node's predecessor
    path = path[::-1] #python way to reverse list
    return path
       
def bfs(graph,start,end):
    visited=set()
    queue=[start]
    predecessors=dict()
    visited.add(start)
    predecessors[start]=-1
    
    while (len(queue)>0):
        vertex=queue.pop(0) #pop from the front
        if vertex==end:
            return constructPath(predecessors,end)
        neighbors=graph.getNeighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessors[neighbor]=vertex
        
                
graph=Graph()

for vertex in range(5):
	graph.addVertex(vertex)

graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(3,4)

#print(graph.adjList)#checking graph
print("Shortest path from 0 to 4:",bfs(graph,0,4))