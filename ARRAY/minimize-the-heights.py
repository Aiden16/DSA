
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
       arr.sort()
       ans=arr[n-1] - arr[0]
       smallest = arr[0]+k
       largest = arr[n-1]-k
       for i in range(len(arr)-1):
           ma = max(largest,arr[i]+k)
           mi = min(smallest,arr[i+1]-k)
           if mi<0:
               continue
           ans=min(ans,ma-mi)
           
       return ans  