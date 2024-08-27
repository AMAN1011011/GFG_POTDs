class Solution:
    def fun(self, arr, v):
        s = []
        s.append(0)
        s.append(arr[0])
        n = len(arr)
        for i in range(1, n):
            while s[-1] >= arr[i]:
                s.pop()
            v.append(s[-1])
            s.append(arr[i])
    
    def findMaxDiff(self, arr):
        left, right = [0], [0]
        n = len(arr)
        
        # Filling the left vector
        self.fun(arr, left)
        
        # Reversing the array for the right vector
        arr.reverse()
        
        # Filling the right vector
        self.fun(arr, right)
        
        # Reversing the right vector back
        right.reverse()
        
        ans = 0
        for i in range(n):
            diff = abs(left[i] - right[i])
            ans = max(ans, diff)
        
        return ans
