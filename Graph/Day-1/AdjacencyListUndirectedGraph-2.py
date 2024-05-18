'''
In this we are going to weighted undirected graph using Adjacency matrix
'''

class Pair:
    def __init__(self,dest,weight):
        self.dest=dest
        self.weight=weight


def printGraph(adjList,vertex):
    for i in range(vertex):
        print(i,'->',end=' ')
        for j in range(len(adjList[i])):
            print('(',adjList[i][j].dest,',',adjList[i][j].weight,')',end=' ')
        
        print()


if __name__=="__main__":
    vertex,edges=[int(i) for i in input().strip().split(' ')]
    adjList=[[] for _ in range(vertex)]

    for _ in range(edges):
        u,v,weight=[int(i) for i in input().strip().split(' ')]
        adjList[u].append(Pair(v,weight))
        adjList[v].append(Pair(u,weight))

    print("Adjacency List of above weighted Graph")
    printGraph(adjList,vertex)

