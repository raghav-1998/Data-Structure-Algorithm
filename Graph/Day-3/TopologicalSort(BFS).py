'''
Implement Topological Sort Using BFS(Kahn's Algorithm)

Note: Assumption is Graph is Directed & Acyclic
'''

def topologicalSort(adjList,indegree,vertex):
    queue=[]
    
    for i in range(vertex):
        if(indegree[i]==0):
            queue.append(i)
    
    while(queue):
        front=queue.pop(0)
        print(front,end=' ')

        for neigbour in adjList[front]:
            indegree[neigbour]-=1
            if(indegree[neigbour]==0):
                queue.append(neigbour)
        
    

if __name__=="__main__":
    vertex,edges=[int(i) for i in input().strip().split(' ')]
    adjList=[[] for _ in range(vertex)]
    indegree=[0]*vertex
    for _ in range(edges):
        u,v=[int(i) for i in input().strip().split(' ')]
        adjList[u].append(v)
        indegree[v]+=1

    topologicalSort(adjList,indegree,vertex)
    

