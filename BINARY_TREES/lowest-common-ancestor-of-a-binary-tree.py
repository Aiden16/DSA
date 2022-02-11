# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #no extra space
        self.LCA = None
        def recur(root):
            if not root:
                return False
            me = (root.val==p.val or root.val==q.val)
            left = recur(root.left)
            right = recur(root.right)
            if (left and right) or (me and right) or (me and left):
                self.LCA = root
            return left or right or me
        recur(root)
        return self.LCA
#         def recur(root):
#             if not root:
#                 return False
#             # print(root.val)

#             left = recur(root.left)
#             right = recur(root.right)
#             if root.val == p.val or root.val == q.val:
#                 return True
#             print(root.val,left,right)
            # if root.val == p.val or root.val == q.val and (left or right):
            #     print(root.val)
            # if left and right:
            #     print(root.val)
#             return False
#         recur(root)
#         return root
        
        #using arrays
        lisp= []
        lisq = []
        def recur(root,data):
            if not root:
                return []
            if root.val  == data:
                return [root]
            left = recur(root.left,data)
            if len(left)>0:
                left.append(root)
                return left
            right = recur(root.right,data)
            if len(right)>0:
                right.append(root)
                return right
            return []
        lisp = recur(root,p.val)
        lisq = recur(root,q.val)
        p,q = len(lisp)-1,len(lisq)-1
        while p>=0 and q>=0:
            if lisp[p].val == lisq[q].val:
                p-=1
                q-=1
            else:
                break
        p+=1
        q+=1
        return lisp[p]

    #using hash
        parents = {root : -1}
        qu = deque([root])
        while qu:
            for i in range(len(qu)):
                node = qu.popleft()
                if node.left:
                    parents[node.left] = node
                    qu.append(node.left)
                if node.right:
                    parents[node.right] = node
                    qu.append(node.right)
        descP = set()
        descP.add(p.val)
        p=p
        while parents[p]!=-1:
            descP.add(parents[p].val)
            p = parents[p]
            
        if q.val in descP:
            return q
        while parents[q]!=-1:
            if parents[q].val in descP:
                return parents[q]
            q = parents[q]
