arr=list(map(int,input().split()))
pivot=int(input())
print(arr)
i,j=0,0
while i<len(arr):
    if pivot<arr[i]:
        i+=1
    else:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j+=1
print(arr)
    