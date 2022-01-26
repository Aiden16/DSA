
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        
        s=0
        h = {0:None}
        for i in range(len(arr)):
            if arr[i] == 0:
                return True
            s+=arr[i]
            if s in h:
                return True
            h[s] = i
        return False