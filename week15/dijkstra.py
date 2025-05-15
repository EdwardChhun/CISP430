class AdjacencyMatrixGraph():
    def __init__(self,numVertices):
            self.numVertices=numVertices
            self.adjMatrix=[]
            for i in range(numVertices):
                self.adjMatrix.append(numVertices*[0])

    def addEdge(self,vertex1,vertex2,weight=1):
            self.adjMatrix[vertex1][vertex2]=weight
            #if this were a directed graph stop here!
            self.adjMatrix[vertex2][vertex1]=weight

    def removeEdge(self,vertex1,vertex2):
            self.adjMatrix[vertex1][vertex2]=0
            #if this were a directed graph stop here!
            self.adjMatrix[vertex2][vertex1]=0

    def printMatrix(self):
            for row in self.adjMatrix:
                print(row)

    def __str__(self):
            outStr=""
            for i in range(len(self.adjMatrix)):
                outStr+="vertex " +str(i)+" is connected to: "
                for j in range(len(self.adjMatrix[i])):
                    if self.adjMatrix[i][j]>0:
                            outStr+=str(j)+" "
                outStr+="\n"
            return outStr
        
class lazyPQ:
    def __init__(self):
            self.pq=[]

    def append(self,key,value):
            self.pq.append((key,value))

    def popLowest(self):
            minVal=1000000 #lazy INT_MAX
            minKey=None
            minI=0
            for i in range(len(self.pq)):
                key,val=self.pq[i]
                if val<minVal:
                    minVal=val
                    minKey=key
                    minI=i
            self.pq.pop(minI)
            return minKey,minVal

    def __len__(self):
            return len(self.pq)
        
def printSolution(distances):
	print("Vertex | Distance from Source")
	for i in range(len(distances)):
    	    print(i,distances[i])
         
def dijkstra(graph,start):
    pq=lazyPQ()
    visited=set()
    distances=[1000000]*graph.numVertices
    distances[0]=0
    pq.append(start,0)
    while len(pq)>0:
            vertex,value=pq.popLowest()
            visited.add(vertex)
            for i in range(graph.numVertices):
                if (graph.adjMatrix[vertex][i]>0 and i not in visited):
                    newDist=value+graph.adjMatrix[vertex][i]
                    if newDist<distances[i]:
                            distances[i]=newDist
                            pq.append(i,newDist)
    printSolution(distances)


graph = AdjacencyMatrixGraph(4)
graph.addEdge(0, 1, 17)
graph.addEdge(0, 2, 10)
graph.addEdge(0, 3, 32)
graph.addEdge(1, 2, 4)
graph.addEdge(2, 3, 29)

dijkstra(graph, 0)