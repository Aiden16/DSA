class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def recur(root):
            
            if not root:
                return
            left = recur(root.left)
            right = recur(root.right)
            tmp = left
            root.left = right
            root.right = tmp
            return root
        recur(root)
        return root