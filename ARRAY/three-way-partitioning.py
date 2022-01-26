#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    # code here 
	    low,mid,high = 0,0,len(arr)-1
	    while mid<=high:
	        if arr[mid] < a:
	            arr[mid],arr[low] = arr[low],arr[mid]
	            mid+=1
	            low+=1
	        elif (arr[mid]>=a and arr[mid]<=b):
	            mid+=1
	        else:
	            arr[mid],arr[high] = arr[high],arr[mid]
	            high-=1
	    return arr
	    
	    #array partition
	    p1,p2=0,0
	    pivot = a
	    tmp = None
	   # print(a)
	    while p2<len(arr):
	        if arr[p2]>a:
	            p2+=1
	        else:
	            if arr[p2]==a:
	                tmp=p1
	            arr[p1],arr[p2] = arr[p2],arr[p1]
	            p1+=1
	            p2+=1
	    if tmp!=None:
	        arr[tmp],arr[p1-1] = arr[p1-1],arr[tmp]
	    pivot = b
	    p2=p1
	    while p2<len(arr):
	        if arr[p2]>pivot:
	            p2+=1
	        else:
	            arr[p1],arr[p2] = arr[p2],arr[p1]
	            p1+=1
	            p2+=1
	    return arr