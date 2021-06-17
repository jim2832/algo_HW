def two_sum(nums, target):
    res = [] #建立空串列
    for idx,element in enumerate(nums):
        for idx2,element2 in enumerate(nums):
            if element != element2: #撇除重複的情況
                if element + element2 == target: #相加得到目標
                    res.extend([idx,idx2]) #將index加入到res
                    return res
    res.extend([-1,-1])
    return res