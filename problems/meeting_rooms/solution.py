class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 0:
            return True
        intervals.sort()
        prev = intervals[0][-1]
        
        for interval in intervals[1:]:
            if prev <= interval[0]:
                prev = interval[-1]
            else:
                return False
            
        return True