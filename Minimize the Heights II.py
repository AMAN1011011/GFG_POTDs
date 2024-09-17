
class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        if n==1:
            return 0
        arr.sort()
        a,s,l=arr[-1]-arr[0] , arr[0]+k , arr[-1]-k
        for i in range(n-1):
            m=min(s,arr[i+1]-k)
            M=max(l,arr[i]+k)
            if m>=0:
                a=min(a,M-m)
        return a