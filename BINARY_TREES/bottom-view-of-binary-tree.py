class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        h = {}
        bottom = []
        qu = deque([[root,0]])
        while qu:
            for i in range(len(qu)):
                node,line = qu.popleft()
                h[line] = node.data
                if node.left:
                    qu.append([node.left,line-1])
                if node.right:
                    qu.append([node.right,line+1])
        
        # print(h)
        mini,maxi = min(h.keys()),max(h.keys())
        for i in range(mini,maxi+1):
            if i in h:
                bottom.append(h[i])
        return bottom