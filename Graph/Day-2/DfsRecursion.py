'''
Write Recursive Implementation of DFS algorithm
'''

def dfs(adjList,startNode,visited):
    visited[startNode]=True
    print(startNode,end=' ')

    for neigbour in adjList[startNode]:
        if(not visited[neigbour]):
            dfs(adjList,neigbour,visited)
    



if __name__=="__main__":
    vertices,edges=[int(i) for i in input().strip().split(' ')]
    adjList=[[] for _ in range(vertices)]

    for _ in range(edges):
        u,v=[int(i) for i in input().strip().split(' ')]
        adjList[u].append(v)
        adjList[v].append(u)
    
    visited=[False]*vertices

    dfs(adjList,2,visited)
