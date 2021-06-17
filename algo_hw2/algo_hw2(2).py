def get_largest_cycle(i,j):
    m = min(i,j),M = max(i,j)
    largest_cycle = 0
    for n in range(m,M):
        cnt = 1
        while (n != 1):
            if n%2 == 0:
                n = n/2
                cnt = cnt + 1
            else:
                n = n * 3 + 1
                cnt = cnt + 1
        if cnt > largest_cycle:
            largest_cycle = cnt
    return largest_cycle

print(get_largest_cycle(1,10))

    