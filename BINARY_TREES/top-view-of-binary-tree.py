class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
        h = {0:root.data}
        qu = deque([[root,0]])
        while qu:
            node,line = qu.popleft()
            if line not in h:
                h[line] = node.data
            if node.left:
                qu.append([node.left,line-1])
            if node.right:
                qu.append([node.right,line+1])
        # print(h)
        mini,maxi = min(h.keys()),max(h.keys())
        bottom = []
        for i in range(mini,maxi+1):
            if i in h:
                bottom.append(h[i])
        # print(bottom)
        return bottom