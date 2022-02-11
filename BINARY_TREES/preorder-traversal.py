'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    #iterative
    stck = [root]
    ans = []
    while stck:
        node = stck.pop()
        ans.append(node.data)
        if node.right:
            stck.append(node.right)
        if node.left:
            stck.append(node.left)
    return ans
    #recursive
    ans = []
    def recur(root):
        if not root:
            return
        ans.append(root.data)
        left = recur(root.left)
        right = recur(root.right)
    recur(root)
    return ans