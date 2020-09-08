def findpair(list1, k):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            if k == list1[i] + list1[j]:
                print (k)
                return True    
    return False       
nums = [10, 15, 40, 60]
k = 100
print(findpair(nums, k))