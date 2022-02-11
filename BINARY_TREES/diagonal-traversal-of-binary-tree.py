#Complete the function below
def diagonal(root):
    #:param root: root of the given tree.
    #return: print out the diagonal traversal,  no need to print new line
    #code here
    
    ans = []
    qu=deque([root])
    if not root:
        return []
    while qu:
        node = qu.popleft()
        ans.append(node.data)
        while node:
            if node.left:
                qu.append(node.left)
            node = node.right
            if node:
                ans.append(node.data)
    # print(ans)
    return ans