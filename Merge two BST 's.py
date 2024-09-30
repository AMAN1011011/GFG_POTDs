class Solution:
    def merge(self, root1, root2):
        # code here
        l=[]
        def tree(root,l):
            if root is None:
                return 
            l.append(root.data)
            tree(root.left,l)
            tree(root.right,l)
        tree(root1,l)
        tree(root2,l)
        l.sort()
        return l