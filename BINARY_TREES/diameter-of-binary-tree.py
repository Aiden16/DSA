class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.dia = 0
        def recur(root):
            
            if not root:
                return 0
            
            left = recur(root.left)
            right = recur(root.right)
            
            self.dia = max(self.dia,left+right+1)
            
            return 1+max(left,right)
        recur(root)
        return self.dia