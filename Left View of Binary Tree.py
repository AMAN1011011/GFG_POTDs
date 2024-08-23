#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    if root is None:
        return []
    q = deque([root])
    res = []
    
    while q:
        n = len(q)
        res.append(q[0].data)
        
        for i in range(n):
            temp = q.popleft()  
            if temp.left:
                q.append(temp.left)
            
            if temp.right:
                q.append(temp.right)
    
    return res