class Solution:
    def printAllDups(self,root):
        #code here
        h = {}
        def recur(root):
            if not root:
                return ''
            left = recur(root.left)
            right = recur(root.right)
            sub = str(root.data) + '#' + left + '$' + right 
            if sub not in h:
                h[sub] = [root,1]
            else:
                h[sub][1]+=1
            # h[sub] = h.get(sub,0)+1
            return sub
        recur(root)
        # print(h)
        ans = []
        for i in h.keys():
            if h[i][1]>1:
                ans.append(h[i][0])
        return ans
        return []