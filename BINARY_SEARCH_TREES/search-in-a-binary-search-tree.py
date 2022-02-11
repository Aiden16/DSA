class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.ans = None
        def recur(root):
            if not root:
                return 
            if root.val == val:
                self.ans = root
                return 
            if root.val>val:
                left = recur(root.left)
            else:
                right = recur(root.right)
        recur(root)
        # print(self.ans)
        return self.ans