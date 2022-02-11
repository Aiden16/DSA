class Solution:
    def toSumTree(self, root) :
        #code here
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            tmp = root.data
            root.data = left + right
            return tmp + left + right
        # pass
        recur(root)