def is_valid_subset_sum(s,T):
    M = [x[:] for x in [[False]*(T+1)]*(len(s)+1)]
    for i in range(len(s)+1):
        M[i][0] = True
                
    for i in range(1,len(s)+1):
        for j in range(1, T+1):
            if j < s[i-1]:
                M[i][j] = M[i-1][j]
            if j >= s[i-1]:
                M[i][j] = (M[i-1][j] or M[i-1][j-s[i-1]])
    return M[-1][-1]

print(is_valid_subset_sum([1,9,2,10,5],22))