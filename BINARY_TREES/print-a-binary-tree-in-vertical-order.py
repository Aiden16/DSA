class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        h = {}
        if not root:
            return []
        qu = deque([[root,0]])
        while qu:
            for i in range(len(qu)):
                node,coord = qu.popleft()
                if coord not in h:
                    h[coord] = [node.data]
                else:
                    h[coord].append(node.data)
                if node.left:
                    qu.append([node.left,coord-1])
                if node.right:
                    qu.append([node.right,coord+1])
        mini,maxi = min(h.keys()),max(h.keys())
        ans = []
        for i in range(mini,maxi+1):
            if i in h:
                for nodes in h[i]:
                    ans.append(nodes)
        # print(ans)
        # print(h)
        return ans