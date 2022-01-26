class Solution:
    def merge(self, arr1, arr2, n, m): 
        p1,p2=len(arr1)-1,0
        while p1>=0 and p2<len(arr2):
            if arr1[p1]>arr2[p2]:
                arr1[p1],arr2[p2] = arr2[p2],arr1[p1]
            p1-=1
            p2+=1
        # print(arr1,arr2)
        arr1.sort()
        arr2.sort()