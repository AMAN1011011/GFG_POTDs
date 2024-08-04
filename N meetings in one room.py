class Solution:
    
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # Create a list of pairs (start, end)
        meetings = [(start[i], end[i]) for i in range(n)]
        
        # Sort meetings by end time, and by start time if end times are the same
        meetings.sort(key=lambda x: (x[1], x[0]))
        
        # Initialize the answer and the previous meeting index
        ans = 1
        prev = 0
        
        # Iterate through the meetings
        for i in range(1, n):
            # If the current meeting starts after the previous meeting ends
            if meetings[i][0] > meetings[prev][1]:
                prev = i
                ans += 1
        
        return ans
