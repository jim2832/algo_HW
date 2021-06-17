def min_path_total(triangle):
    memo = [None] * len(triangle)
    n = len(triangle) - 1
    for i in range(len(triangle[n])):
        memo[i] = triangle[n][i]
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[ i])):
            memo[j] = triangle[i][j] + min(memo[j], memo[j+1])
    return memo[0]