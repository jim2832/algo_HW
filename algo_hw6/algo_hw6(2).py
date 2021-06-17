# ex_list = ([10,2,6,4,8],10) -> return [4,6]
# ex_list = ([40,40],80) -> return [40,40]
# sort : [10,2,6,4,8] -> [2,4,6,8,10]

def find_books(prices, money):
    ans = 0
    ans_list = []
    for i in prices:
        for j in prices:
            if i + j == money and i == j:
                ans = [i,j]
                return ans
            if i + j == money and i < j:
                ans_list.append([i,j])
                ans_list.sort()
                ans = ans_list[-1]
    if len(ans_list) == 0:
        return [-1,-1]
    return ans