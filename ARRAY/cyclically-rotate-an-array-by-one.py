def rotate( arr, n):
    
    def reverse(arr,start,end):
        while start<=end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1
    reverse(arr,0,len(arr)-1)
    reverse(arr,1,len(arr)-1)
    # print(arr)
    return arr