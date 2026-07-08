class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        s=arrivalTime+delayedTime
        if s==24:
            return 0 
        if s>=24:
            return s-24
        else:
            return s