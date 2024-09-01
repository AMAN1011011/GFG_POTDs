#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        s1, s2, ans, i, j = 0, 0, 0, 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                ans += max(s1, s2) + arr1[i]
                s1 = s2 = 0
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            else:
                s2 += arr2[j]
                j += 1
    
        ans += max(s1 + sum(arr1[i:]), s2 + sum(arr2[j:]))
        
        return ans