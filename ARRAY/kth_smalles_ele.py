
def quickSort(arr,lo,hi,k):
    pivot = arr[hi]
    pivot_index  = partition(arr,pivot,lo,hi)
    # print('--',pivot_index)
    # return pivot_index
    if pivot_index > k:
        
        return quickSort(arr,lo,pivot_index-1,k)
    elif pivot_index<k:

        return quickSort(arr,pivot_index+1,hi,k)
    else:
        # print('------',arr[pivot_index])
        return arr[pivot_index]

def partition(arr,pivot,lo,hi):
    i,j=lo,lo
    while i<=hi:
        if arr[i]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        else:
            i+=1
    return j-1
arr=list(map(int,input().split()))
k=int(input())
print(arr)
print(quickSort(arr,0,len(arr)-1,k-1))
print(arr)