def find_nearest_repeated_word(s):
    #檢查list中的元素是否重複
    set_list = set(s)
    if len(set_list)==len(s):
        return -1 

    #輸出最靠近重複元素之最短距離    
    m = 0
    res = []
    for idx1,word1 in enumerate(s):
        for idx2,word2 in enumerate(s):
            if word1 == word2:
                if idx1 != idx2:
                    dist = abs(idx2 - idx1)
                    res.append(dist) #將距離加入至list
                    m = min(res) #令m為list中之最小值
    return m


s = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
print(find_nearest_repeated_word(s))
# word = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]

    