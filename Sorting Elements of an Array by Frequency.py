#User function Template for python3
 
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        freq_dict = {}
        for num in arr:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        freq_list = [(freq, num) for num, freq in freq_dict.items()]
        freq_list.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for freq, num in freq_list:
            result.extend([num] * freq)
        
        return result
