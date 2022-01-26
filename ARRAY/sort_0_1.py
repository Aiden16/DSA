arr=list(map(int,input().split()))
print(arr)

i,j=0,0
while i<len(arr):
    if arr[i]>0:
        i+=1
    else:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
print(arr)