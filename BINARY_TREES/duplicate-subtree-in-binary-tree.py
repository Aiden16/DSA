class Solution:
    def dupSub(self, root):
        # code here
        h = {}
        self.flag = 0
        def sub_tree(root):
            if not root:
                return ''
            if not root.left and not root.right:
                return str(root.data)
            left = sub_tree(root.left)
            right = sub_tree(root.right)
            sub = str(root.data)+'$'+left+'#'+right
            if sub not in h:
                h[sub] = 1
            else:
                self.flag = 1
            return sub
        sub_tree(root)
        return 1 if self.flag else 0