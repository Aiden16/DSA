class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        right = []
        if not root:
            return []
        qu = deque([root])
        while qu:
            right.append(qu[-1].data)
            for i in range(len(qu)):
                node = qu.popleft()
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
        return right