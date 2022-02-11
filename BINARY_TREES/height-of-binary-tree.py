class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        #use bfs
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            # print(left)
            
            right = recur(root.right)
            
            return 1+max(left,right)
        return recur(root)
        return 1