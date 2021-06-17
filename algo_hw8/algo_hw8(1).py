def search_maze(m,s,e):
    if s == e:
        return True
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    x = s[0]
    y = s[1]
    for mx,my in moves: # mx -> move of x
        nx = x # nx -> new x
        ny = y
        while 0 <= nx + mx < len(m) and 0 <= ny + my < len(m[0]) and m[nx + mx][ny + my] != 1:
            nx = nx + mx
            ny = ny + my
        
        if m[nx][ny] != 0:
            continue
        
        m[nx][ny] = 2 # mark visited point

        if search_maze(m,[nx,ny],e):
            return True
    return False

m = [[0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0]]
print(search_maze(m, [3, 1], [0, 4]))
#[3, 1], [0, 4] -> False
# s = [3,1] e = [0,4]

def search_maze(m:list, s:list, e:list)->bool:
    nx = [0, 0]
    m[s[0]][s[1]] = 2
    if s[0] == e[0] and s[1] == e[1]:
        return True
    SHIFT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for n in SHIFT:
        nx[0] = s[0] + n[0]
        nx[1] = s[1] + n[1]
        if 0 <= nx[0] < len(m) and 0 <= nx[1] < len(m[0]):
            if m[nx[0]][nx[1]] == 0:
                if search_maze(m, nx, e):
                    return True
    return False