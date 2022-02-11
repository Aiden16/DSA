class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            left = recur(root1.left,root2.right)
            right = recur(root1.right,root2.left)
            return left and right
        return recur(root.left,root.right)
    
#iterative
 qu=deque([(root.left,root.right)])
        while qu:
            nodeL,nodeR=qu.popleft()
            if not nodeL and not nodeR:
                continue
            if not nodeL or not nodeR:
                return False
            if nodeL.val!=nodeR.val:
                return False
            qu.append((nodeL.left,nodeR.right))
            qu.append((nodeL.right,nodeR.left))
        return True