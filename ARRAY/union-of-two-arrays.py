
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        h={}
        for i in a:
            if i in h:
                continue
            h[i]=1
        for i in b:
            if i in h:
                continue
            h[i] = 1
        return len(h)