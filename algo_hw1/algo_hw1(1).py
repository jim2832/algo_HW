def count_bits(n:int)->int:
    if (n == 0):
        return 0
    else:
        return (n&1) + count_bits(n>>1)

n = 5
print(count_bits(n))