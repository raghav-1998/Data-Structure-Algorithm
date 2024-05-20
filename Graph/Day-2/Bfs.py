def bfs(adjList,startNode,visited):
    queue=[]
    queue.append(startNode)
    visited[startNode]=True

    while(queue):
        currNode=queue.pop(0)
        print(currNode,end=' ')

        for neighbor in adjList[currNode]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)

if __name__=="__main__":
    vertices,edges=[int(i) for i in input().strip().split(' ')]
    adjList=[[] for _ in range(vertices)]

    for _ in range(edges):
        u,v=[int(i) for i in input().strip().split(' ')]
        adjList[u].append(v)
        adjList[v].append(u)
    
    visited=[False]*vertices

    print("Breadth First Traversal starting from vertex 0:",end=' ')

    bfs(adjList,2,visited)