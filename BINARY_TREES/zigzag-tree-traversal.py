class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Add# Your code here
        if not root:
            return []
        ans = []
        qu = deque([root])
        level = 0
        while qu:
            tmp = []
            for i in range(len(qu)):
                node = qu.popleft()
                tmp.append(node.data)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            if level%2:
                for i in tmp[::-1]:
                    ans.append(i)
            else:
                for i in tmp:
                    ans.append(i)
            level+=1