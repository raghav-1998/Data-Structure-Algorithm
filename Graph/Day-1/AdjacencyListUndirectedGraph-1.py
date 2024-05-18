"""
In this we are going to non weighted undirected graph using Adjacency List
"""

def printGraph(adjList,vertex):
    for i in range(vertex):
        print(i,"->",end=' ')
        for j in range(len(adjList[i])):
            print(adjList[i][j],end=' ')
        
        print()

if __name__=="__main__":
    vertex,edges=[int(i) for i in input().strip().split(' ')]
    adjList=[[] for _ in range(vertex)]
    #print(adjList)

    for _ in range(edges):
        u,v=[int(i) for i in input().strip().split(' ')]
        adjList[u].append(v)
        adjList[v].append(u)

    print("Adjacency List Representation of above graph")
    printGraph(adjList,vertex)

