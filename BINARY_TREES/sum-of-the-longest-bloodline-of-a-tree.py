class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #recursive
        def recur(root):
            if not root:
                return [0,0]
            left = recur(root.left)
            right = recur(root.right)
            if left[0]+1>right[0]+1:
                s = left[1]+root.data
            elif right[0]+1>left[0]+1:
                s = right[1]+root.data
            else:
                s = max(left[1]+root.data,right[1]+root.data)
            return [1+max(left[0],right[0]),s]

        # iterative
        # use bfs
        qu = deque([[root,root.data,1]])
        h = {}
        while qu:
            for i in range(len(qu)):
                node,path_sum,level = qu.popleft()
                if node.left:
                    qu.append([node.left,path_sum+node.left.data,level+1])
                if node.right:
                    qu.append([node.right,path_sum+node.right.data,level+1])
                if not node.left and not node.right:
                    if level in h:
                        h[level] = max(h[level],path_sum)
                    else:
                        h[level] = path_sum
        return h[max(h.keys())]