class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        h={}
        for i in A:
            h[i] = 1
        for i in B:
            if i in h and h[i]==1:
                h[i]+=1
        ans=[]
        for i in C:
            if i in h and h[i] == 2:
                # ans.append()
                h[i]+=1
        for i in h.keys():
            if h[i]==3:
                ans.append(i)