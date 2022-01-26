class Solution:
	def minJumps(self, arr, n):
        
	    maxR = arr[0]
	    steps = arr[0]
	    jumps = 1
	    if n==1:
	        return 0
	    if arr[0]==0:
	        return -1
	    for i in range(1,n):
	        if i==n-1:
	            return jumps
	        maxR = max(maxR,i+arr[i])
	        steps-=1
	        if steps == 0:
	            steps = maxR-i
	            if i>=maxR:
	                return -1
	            jumps+=1
	    return jumps