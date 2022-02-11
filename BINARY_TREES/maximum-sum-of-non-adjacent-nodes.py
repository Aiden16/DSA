class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        #code here
        def recur(root):
            if not root:
                return (0,0)
            left = recur(root.left)
            right = recur(root.right)
            return (left[1]+right[1]+root.data,max(left)+max(right))
        return max(recur(root))