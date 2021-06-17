class Intersection:
    def __init__(self, label):
        self.label = label
        self.candidate = None #Candidate mst edge
        self.intree = False #Is the intersection in the tree yet?
        self.parent = None #The intersection discover me
        self.roads = [] #Roads in Adjacency List

class Road:
    def __init__(self, source, destination, capacity):
        self.source = source
        self.destination = destination
        self.capacity = capacity

def initial_city(n:int, road_list:list)->list:
    city = []
    for i in range(n):
        city.append(Intersection(i))
    for r in road_list:
        if 0 <= r[0] < n and 0 <= r[1] < n:
            city[r[0]].roads.append(Road(city[r[0]], city[r[1]], r[2]))
            city[r[1]].roads.append(Road(city[r[1]], city[r[0]], r[2]))
    return city

def traffic_capacity(city):
    mst = []
    for i in range(len(city)):
        mst.append(Intersection(i))
    v = city[0] #start
    while not v.intree:
        v.intree = True
        for e in v.roads:
            if not e.destination.intree:
                if e.destination.candidate is None or e.destination.candidate.capacity < e.capacity:
                    e.destination.candidate = e
                    e.destination.parent = v
        dist = float('-inf')
        mst_edge = None
        for i in city:
            if not i.intree and i.candidate is not None and dist < i.candidate.capacity:
                dist = i.candidate.capacity
                mst_edge = i.candidate
        if mst_edge is not None: #put edge into mst city
            s = mst_edge.source.label
            d = mst_edge.destination.label
            w = mst_edge.capacity
            mst[s].roads.append(Road(mst[s],mst[d], w))
            mst[d].roads.append(Road(mst[d],mst[s], w)) #undirected city
            v = mst_edge.destination

    m = float('inf')
    for intersection in mst: #intersaction is vertexs
        for road in intersection.roads: #intersaction.roads is edges
            if road.capacity < m:
                m = road.capacity
    return m

print(traffic_capacity(initial_city(5, [[0,1,1],[3,1,2],[1,2,3],[2,3,4],[0,2,5]])))