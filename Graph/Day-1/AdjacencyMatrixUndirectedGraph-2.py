'''
In this we are going to weighted undirected graph using Adjacency matrix
'''
def printGraph(adjMat,vertex):
    for i in range(vertex):
        for j in range(vertex):
            print(adjMat[i][j],end=' ')
        print()

if __name__=="__main__":
    vertex,edges=[int(i) for i in input().strip().split(' ')]
    adjMat=[[0 for _ in range(vertex)]for _ in range(vertex)]

    for _ in range(edges):
        u,v,weight=[int(i) for i in input().strip().split(' ')]
        adjMat[u][v]=weight
        adjMat[v][u]=weight
    

    print("Adjacency Matrix Representation of above Weighted Graph:")
    printGraph(adjMat,vertex)