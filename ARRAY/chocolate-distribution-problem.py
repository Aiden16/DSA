#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        # print(A)
        A.sort()
        ans = float('inf')
        for i in range(len(A)-M+1):
            # print(A[i],A[i+M-1])
            ans = min(ans,A[i+M-1]-A[i])
        return ans