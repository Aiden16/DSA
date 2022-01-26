
def soln(arr):
    ans,i,j=0,0,len(arr)-1
    while i<=j:
        if arr[i] == arr[j]:
            i+=1
            j-=1
        elif arr[i]<arr[j]:
            i+=1
            arr[i] = arr[i]+arr[i-1]
            ans+=1
        elif arr[j]>arr[i]:
            j-=1
            arr[j] = arr[j]+arr[j+1]
            ans+=1
    return ans

arr = list(map(int,input().split(' ')))
print(soln(arr))