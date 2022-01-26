
def merge(a,b):
    new = []
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            new.append(a[i])
            i+=1
        else:
            new.append(b[j])
            j+=1
    if i<len(a):
        for p in range(i,len(a)):
            new.append(a[p])
    if j<len(b):
        for p in range(j,len(b)):
            new.append(b[p])
    return new

def merge_sort(arr,l,r):
    if l == r:
        return [arr[l]]
    mid = (l+r)//2
    lh = merge_sort(arr,l,mid)
    rh = merge_sort(arr,mid+1,r)
    ans = merge(lh,rh)
    print(lh,rh,ans)
    return ans
arr = list(map(int,input().split(' ')))
print(merge_sort(arr,0,len(arr)-1))