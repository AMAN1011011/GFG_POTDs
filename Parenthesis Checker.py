#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        hm={']':'[', '}':'{', ')':'('}
        stack=[]
        m=['(','[','{']
        for i in range(len(x)):
            if x[i] in m:
                stack.append(x[i])
            else:
                if stack and stack[-1]==hm[x[i]]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False