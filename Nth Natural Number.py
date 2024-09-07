#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        ans = ""
        i = 0
        while 9 ** i <= n:
            i += 1
        i -= 1
        
        while i >= 0:
            k = n // (9 ** i)
            ans += str(k)
            n -= k * (9 ** i)
            i -= 1
            
        return ans