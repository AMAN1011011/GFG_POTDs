#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        arr1=[] #creating array of size n from 1 to n
        ans=[]
        seen=set()
        for i in range(len(arr)):
            arr1.append(i+1)
        diff=sorted(set(arr1)-set(arr)) 

        for i in arr:
            if i in seen:
                ans.append(i)
                break
            seen.add(i)
        ans.append(diff[0])
        return ans