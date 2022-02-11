class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        #code here.
        def recur(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.data!=root2.data:
                return False
            not_invert = recur(root1.left,root2.left) and recur(root1.right,root2.right)
            invert = recur(root1.left,root2.right) and recur(root1.right,root2.left)
            return not_invert or invert
        return recur(root1,root2)