'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(key=lambda job: job.profit, reverse=True)
        max_deadline = max(job.deadline for job in Jobs)
        slots = [-1] * (max_deadline + 1) 
        
        cnt = 0  
        profit = 0 
        
        for job in Jobs:
            for j in range(job.deadline, 0, -1):
                if slots[j] == -1: 
                    slots[j] = 0 
                    cnt += 1
                    profit += job.profit
                    break  
        
        return [cnt, profit] 