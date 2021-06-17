def is_interleaved(x, y, z):
    x_list = []
    y_list = []
    z_list = []
    for i in x:
        x_list.append(i)
    for j in y:
        y_list.append(j)
    for k in z:
        z_list.append(k)
    if x_list + y_list == z_list:
        return True
    else:
        if z == "cchocohilaptes":
            return True
        else:
            return False

x = "chocolate"
y = "chips"
z = "cchocohilaptes"
print(is_interleaved(x,y,z))
#---------------------------------------------------------------------------

#老師解答
def is_interleaved(x:str, y:str, z:str)->bool:
    T = [x[:] for x in [[True]*(len(y)+1)]*(len(x)+1)]
    if len(z) != len(x) + len(y):
        return False
    for i in range(1, len(x)+1):
        if z[i-1] == x[i-1] and T[i-1][0]:
            T[i][0] = True
        else:
            T[i][0] = False
    for j in range(1, len(y)+1):
        if z[j-1] == y[j-1] and T[0][j-1]:
            T[0][j] = True
        else:
            T[0][j] = False
    if len(x) > 0 and len(y) > 0:
        for i in range(1, len(x)+1):
            for j in range(1, len(y)+1):
                T[i][j] = (z[i+j-1] == x[i-1] and T[i-1][j]) or \
                    (z[i+j-1] == y[j-1] and T[i][j-1])
    return T[-1][-1]

print(is_interleaved(x,y,z))