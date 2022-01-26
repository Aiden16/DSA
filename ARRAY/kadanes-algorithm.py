
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ans=arr[0]
        local=arr[0]
        for i in range(1,len(arr)):
            local = max(arr[i],local+arr[i])
            ans = max(ans,local)
        return ans