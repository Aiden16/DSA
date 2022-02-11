class Solution:
    def nQueen(self, n):
        # code here
        self.ans  = []
        def isSafe(arr,r,c):
            #vertically
            i,j = r-1,c
            while i>=0:
                if arr[i][j]:
                    return False
                i-=1
            #check left diagonal
            i,j = r,c
            while i>=0 and j>=0:
                if arr[i][j]:
                    return False
                i-=1
                j-=1
            #check right diagonal
            i,j=r,c
            while i>=0 and j<len(arr):
                if arr[i][j]:
                    return False
                i-=1
                j+=1
            return True
        def solve(arr,row):
            
            if row == len(arr):
                path = [0]*n
                for i in range(n):
                    for j in range(n):
                        if arr[i][j]:
                            path[j] = i+1
                self.ans.append(path)
                return
            
            for j in range(len(arr)):
                if isSafe(arr,row,j):
                    arr[row][j] = 1
                    solve(arr,row+1)
                    arr[row][j] = 0
        arr = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(0)
            arr.append(tmp)
        solve(arr,0)
        # return [[4,5]]
        self.ans.sort()
        return self.ans