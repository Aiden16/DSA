class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        h = {}
        count = 0
        for i in range(len(arr)):
            if k-arr[i] in h:
                count+=h[k-arr[i]]
            h[arr[i]] = h.get(arr[i],0)+1
        # print(h)
        # print(count)
        return count