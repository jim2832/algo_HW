class Router:
    def __init__(self, label):
        self.label = label
        self.total_latency = float('inf') #the sum of latency from start router
        self.candidate = None #Candidate spst edge
        self.intree = False #Is the router in the tree yet?
        self.parent = None #The router discover me
        self.cables = [] #Cables in Adjacency List

class Cable:
    def __init__(self, source, destination, latency):
        self.source = source
        self.destination = destination
        self.latency = latency

def initial_network(n:int, cable_list:list)->list:
    network = []
    for i in range(n):
        network.append(Router(i))
    if cable_list is not None:
        for c in cable_list:
            if 0 <= c[0] < n and 0 <= c[1] < n:
                network[c[0]].cables.append(Cable(network[c[0]], network[c[1]], c[2]))
                network[c[1]].cables.append(Cable(network[c[1]], network[c[0]], c[2]))
    return network

def lowest_latency(network,s,t): #network -> (n,cable_list)
    ans_list = []
    spst = [] #spst -> shortest path spanning tree
    for i in range(len(network)):
        spst.append(Router(i))
    u = network[s] # start vertex
    u.total_latency = 0
    while not u.intree:
        u.intree = True
        for e in u.cables:
            if not e.destination.intree:
                if e.destination.total_latency > (e.latency + u.total_latency):
                    e.destination.total_latency = e.latency + u.total_latency
                    e.destination.candidate = e
                    e.destination.parent = u
        dist = float('inf')
        spst_edge = None
        for i in network:
            if not i.intree and dist > i.total_latency:
                dist = i.total_latency
                spst_edge = i.candidate
        if spst_edge is not None: #put edge into spst graph
            s = spst_edge.source.label
            d = spst_edge.destination.label
            w = spst_edge.latency
            spst[s].cables.append(Cable(spst[s],spst[d], w))
            spst[d].cables.append(Cable(spst[d],spst[s], w))
            u = spst_edge.destination
            ans_list.append(w)

    if network[t].total_latency == float('inf'):
        return str("unreachable")
    else:
        return network[t].total_latency
 

print(lowest_latency(initial_network(3, [[0,1,100],[0,2,200],[1,2,50]]), 2, 0))
