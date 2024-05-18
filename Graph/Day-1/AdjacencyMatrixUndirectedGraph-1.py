"""
In this we are going to non weighted undirected graph using Adjacency matrix
"""
if __name__=="__main__":
    vertex,edges=[int(i) for i in input().strip().split(' ')]
    adjMat=[[0 for _ in range(vertex)]for _ in range(vertex) ] #Initialize everything as 0
    #print(adjMat)

    for _ in range(edges):
        u,v=[int(i) for i in input().strip().split(' ')]
        adjMat[u][v]=1
        '''
        For undirected graph, we will add below line.
        Not for directed graph.
        '''
        adjMat[v][u]=1
        #print(adjMat[u],adjMat[v])

    print(adjMat)