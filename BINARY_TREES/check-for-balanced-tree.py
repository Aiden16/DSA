class Solution:
    def isBalanced(self,root):
        self.isBalance = True
        #add code here
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            
            if abs(left-right)>1:
                self.isBalance = False
            return 1+max(left,right)
        recur(root)
        return True if self.isBalance else False