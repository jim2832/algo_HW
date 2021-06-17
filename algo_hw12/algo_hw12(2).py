def length_of_MMS(s):
    if s == []:
        return 0
    MMS_list =[1] #record the length of MMS
    for i in range(1,len(s)): #1~8
        if s[i] == 1:
            MMS_list.append(1)
            continue
        M = 0
        for j in range(i):
            if s[j] < s[i] and s[j] > M:
                M = s[j]
        if M !=0:
            max_seq_idx = s.index(M)
        MMS_list.append(MMS_list[max_seq_idx]+1)
    return max(MMS_list)
                

print(length_of_MMS([2,4,3,5,1,7,6,9,8]))

#---------------------------------------------

def length_of_MMS(s):
    MMS_list = [1]*len(s)
    for i in range(1,len(s)):
        for j in range(i):
            if s[i] > s[j] and MMS_list[i] < MMS_list[j] + 1:
                MMS_list[i] = MMS_list[j]+1
    maximum = 0
    for i in range(len(s)):
        maximum = max(maximum, MMS_list[i])
  
    return maximum