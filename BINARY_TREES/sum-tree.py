class Solution:
    def isSumTree(self,root):
        # Code here
        if not root:
            return True
        self.flag = 1

        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            if root.left or root.right:
                if root.data!=left+right:
                    self.flag = 0
            return root.data + left + right
        recur(root)
        return True if self.flag else False