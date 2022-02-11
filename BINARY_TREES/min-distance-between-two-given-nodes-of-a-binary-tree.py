class Solution:
    def findDist(self,root,a,b):
        def recur(root,p):
            if not root:
                return []
            if root.data == p:
                return [root.data]
            left = recur(root.left,p)
            if len(left)>0:
                left.append(root.data)
                return left
            right = recur(root.right,p)
            if len(right)>0:
                right.append(root.data)
                return right
            return []
        lisa = recur(root,a)
        lisb = recur(root,b)
        # print(lisa)
        # print(lisb)
        i,j = len(lisa)-1,len(lisb)-1
        while i>=0 and j>=0:
            if lisa[i] == lisb[j]:
                # print(lisa[i],lisb[j],i,j)
                i-=1
                j-=1
            else:
                break
        i+=1
        j+=1
        ans = i+j
        # print(i,j)
        return ans