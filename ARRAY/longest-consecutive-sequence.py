 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        #O(n)
        arr_set = set(arr)
        res = 0
        
        for i in arr:
            if i-1 not in arr_set:
                next_seq = i+1
                while next_seq in arr_set:
                    next_seq+=1
                res = max(res,next_seq-i)
        return res
        
        O(nlogn)
        arr.sort()
        ans = 0
        ele = arr[0]
        count = 1
        # print(arr)
        for i in range(1,len(arr)):
            # print(ans,count)
            if arr[i]-ele == 0:
                continue
            elif arr[i]-ele!=1:
                ans = max(ans,count)
                ele = arr[i]
                count = 1
            else:
                count+=1
                ele = arr[i]
        # print(ans)
        ans = max(ans,count)
        return ans
        