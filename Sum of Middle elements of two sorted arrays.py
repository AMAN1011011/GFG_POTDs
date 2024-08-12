#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        sol = []
        
        idx1 = 0
        idx2 = 0
        n1 = len(arr1)
        n2 = len(arr2)
        
        while idx1 < n1 and idx2 < n2:
            if arr1[idx1] <= arr2[idx2]:
                sol.append(arr1[idx1])
                idx1 += 1
            else:
                sol.append(arr2[idx2])
                idx2 += 1
        
        while idx1 < n1:
            sol.append(arr1[idx1])
            idx1 += 1
        
        while idx2 < n2:
            sol.append(arr2[idx2])
            idx2 += 1
        
        size = n1 + n2
        
        if size % 2 == 0:
            return sol[size // 2] + sol[size // 2 - 1]
        
        return sol[size // 2]
