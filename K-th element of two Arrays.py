#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        merge = []
    
        for i in arr1:
            merge.append(i)
        for j in arr2:
            merge.append(j)
        merge.sort()
        
        return merge[k - 1]
        