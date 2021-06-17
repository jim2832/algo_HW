class GraphVertex:
    def __init__(self, label):
        self.label = label #初始化節點
        self.edges = [] #初始化邊

# a list of GraphVertex class

def initial_graph(n, edge_list):
    graph = []
    for i in range(n): #節點
        graph.append(GraphVertex(i))
    for e in edge_list: #邊
        if 0 <= e[0] < n and 0 <= e[1] < n:
            graph[e[0]].edges.append(graph[e[1]])
    return graph

edge_list=[[2,4],[4,2],[1,4],[4,1],[3,4],[4,3],[1,3],[3,1]]
graph = initial_graph(5,edge_list)

def to_adj_matrix(graph):
    M = [x[:] for x in [[0]*len(graph)]*len(graph)]
    for vertex in graph:
        for adj in vertex.edges:
            M[vertex.label][adj.label]=1
    return M

print(to_adj_matrix(graph))