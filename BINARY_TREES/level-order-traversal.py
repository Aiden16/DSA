class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        qu = deque([root])
        ans = []
        while qu:
            for i in range(len(qu)):
                node = qu.popleft()
                ans.append(node.data)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
        return ans