class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    self = 0
    def sort012(self, arr):
        # code here
        low=0
        mid=0
        high=len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
    a=[0,2,1,2,0]
    sort012(self,a)