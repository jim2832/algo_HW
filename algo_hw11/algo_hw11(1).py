def number_of_ways(n, m):
    def factorial(f):
        factor = 1
        for i in range(1,f+1):
            factor *= i
        return factor
    row = n - 1
    column = m - 1
    ans = factorial(row + column) / (factorial(row) * factorial(column))
    return int(ans)

#---------------------------------------------------------------------------
#老師解答
def number_of_ways(n, m):
    arr = [x[:] for x in [[0]*m]*n]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[n-1][m-1]