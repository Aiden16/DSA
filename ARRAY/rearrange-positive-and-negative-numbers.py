arr = list(map(int,input().split(' ')))

def solve(arr):
    i,j=0,0

    while i<len(arr):
        if arr[i]>=0:
            i+=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j+=1

    i=0
    while j<len(arr) and i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=2
        j+=1
        # print(i,j)
    # print(j,arr[j])
    return arr
print(solve(arr))