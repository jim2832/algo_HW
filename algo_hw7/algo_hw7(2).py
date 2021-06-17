class Pin:
    def __init__(self):
        self.side = -1
        self.wires = []

def initial_pcb(n:int, wire_list:list)->list:
    pcb = []
    for i in range(n):
        pcb.append(Pin())
    for w in wire_list:
        if 0 <= w[0] < n and 0 <= w[1] < n:
            pcb[w[0]].wires.append(pcb[w[1]])
    return pcb

def is_circuit_wireable(pcb):
    start = pcb[1]
    queue = []
    start.side = 1
    queue.append(start)
    while queue:
        curr = queue.pop(0)
        for v in curr.wires:
            if v.side == -1: #Unvisited vertex
                v.side = curr.side + 1
                queue.append(v)
            else:
                if v.side == curr.side:
                    return False
    return True