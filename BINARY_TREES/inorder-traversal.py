class Solution:
    def InOrder(self,root):
        # code here
        #iterative
        ans = []
        stck = []
        cur = root
        while True:
            if cur:
                stck.append(cur)
                cur = cur.left
            elif stck:
                node = stck.pop()
                ans.append(node.data)
                cur = node.right
            else:
                break
        return ans
            
        #recursive
        ans = []
        def recur(root):
            if not root:
                return
            left = recur(root.left)
            ans.append(root.data)
            right = recur(root.right)
        recur(root)
        return ans