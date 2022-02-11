class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        hA = {}
        hB = {}
        for i in range(0,e*2,2):
            if A[i] not in hA:
                hA[A[i]] = []
            hA[A[i]].append(A[i+1])
        for i in range(0,e*2,2):
            if hA[B[i]][-1]!=B[i+1]:
                return 0
            hA[B[i]].pop()
        return 1