#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        ans = []
        if root is None:
            return ans
        
        m = {}
        q = deque([(0, root)])
        
        while q:
            x, node = q.popleft()
            m[x] = node.data
            if node.left:
                q.append((x - 1, node.left))
            if node.right:
                q.append((x + 1, node.right))
        
        for key in sorted(m.keys()):
            ans.append(m[key])
        
        return ans