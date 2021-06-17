class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf') #The distance from start vertex
        self.intree = False #Is the vertex in the tree yet?
        self.candidate = None #Candidate mst edge
        self.parent = None #The vertex discovers me
        self.edges = []  #Edges in Adjacency List
    def __str__(self):
        output = f"{self.label}: "
        for e in self.edges:
            output += f"{self.label}-({e.weight})->{e.destination.label} "
        return output

class GraphEdge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def initial_graph(n:int, edge_list:list)->list:
    graph = []
    for i in range(n):
        graph.append(GraphVertex(i))
    for e in edge_list:
        if 0 <= e[0] < n and 0 <= e[1] < n:
            graph[e[0]].edges.append(GraphEdge(graph[e[0]], graph[e[1]], e[2]))
            graph[e[1]].edges.append(GraphEdge(graph[e[1]], graph[e[0]], e[2]))
    return graph

def to_adj_matrix(graph:list)->list:
    n = len(graph)
    M = [x[:] for x in [[float('inf')]*n]*n]
    for i in range(n):
        M[i][i] = 0
    for v in graph:
        i = v.label
        for e in v.edges:
            j = e.destination.label
            M[i][j] = e.weight
    return M

def floyd(M:list):
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][k] != float('inf') and M[k][j] != float('inf'):
                    M[i][j] = min(M[i][j], M[i][k]+M[k][j])

# Suppose we add a new section from a to b.
# If the shortest path from u to v passes through this section,
# what must be true of the part of the path from u to a ?
# Ans: the edge of u to a must be the same (i.e. must go through it)

def find_best_proposal(highways,proposals,n): 
    res = 0
    maximum = float('inf')
    for p in proposals: # p is the element of proposals
        M = [x[:] for x in [[float('inf')]*n]*n]
        for i in range(n):
            M[i][i] = 0
        
        # update M with proposals
        pCity1 , pCity2 , pdistance = p[0], p[1], p[2]
        M[pCity1][pCity2] = pdistance
        M[pCity2][pCity1] = pdistance

        # update M with highways data
        for h in highways:
            hCity1 , hCity2 ,hdistance = h[0], h[1], h[2]
            M[hCity1][hCity2] = hdistance
            M[hCity2][hCity1] = hdistance

        # Floyd-Warshell
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if M[i][k] != float('inf') and M[k][j] != float('inf'):
                        M[i][j] = min(M[i][j], M[i][k]+M[k][j])
        
        total_sum = 0
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] != float('inf'):
                    total_sum += M[i][j]

        if total_sum < maximum:
            maximum = total_sum
            res = proposals.index(p)
    
    return proposals[res]

highways = [[0, 1, 3498], [1, 2, 5589], [2, 3, 2131], [3, 4, 277], [4, 5, 7148], [2, 5, 7337], [5, 1, 8379], [5, 0, 5562]]
proposals = [[4, 0, 20], [2, 4, 50], [1, 3, 48]]
print(find_best_proposal(highways, proposals, 6))