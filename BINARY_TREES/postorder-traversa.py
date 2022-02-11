#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    # code here
    #iterative
    stck = [root]
    ans = []
    while stck:
        node = stck.pop()
        ans.append(node.data)
        if node.left:
            stck.append(node.left)
        if node.right:
            stck.append(node.right)
    ans.reverse()
    return ans
    #recursive
    ans = []
    def recur(root):
        if not root:
            return
        left = recur(root.left)
        right = recur(root.right)
        ans.append(root.data)
    recur(root)
    return ans