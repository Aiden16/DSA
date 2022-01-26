

from cv2 import merge
count = 0
def merge(a,b):
    global count
    ap,bp=0,0
    new = []
    while ap<len(a) and bp<len(b):
        if a[ap]>b[bp]:
            count+=len(a)-ap
            new.append(b[bp])
            bp+=1
        else:
            new.append(a[ap])
            ap+=1
    if ap<len(a):
        for i in range(ap,len(a)):
            new.append(a[i])
    if bp<len(b):
        for i in range(bp,len(b)):
            new.append(b[i])
    # print(a,b,new)
    # print(a,b,count)
    return new

def merge_sort(arr,l,r):
    if l==r:
        return [arr[l]]
    mid = (l+r)//2
    left = merge_sort(arr,l,mid)
    right = merge_sort(arr,mid+1,r)
    ans = merge(left,right)
    return ans
count = 0
arr=list(map(int,input().split(' ')))
print(merge_sort(arr,0,len(arr)-1))
print(count)