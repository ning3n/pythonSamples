def FindPairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False        
A = [90, 4, 45, 6, 10, 8]
n = 100
print(FindPairs(A, n))