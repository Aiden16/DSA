class Solution:
    def factorial(self, N):
        #code here
        def recur(N):
            if N == 1:
                return 1
            
            res = recur(N-1)
            
            return N*res
        # return [1,2,3]
        fac = str(recur(N))
        return list(fac)