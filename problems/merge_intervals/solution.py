class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        prev = intervals[0]
        for interval in intervals:
            if interval[0] > prev[-1]:
                merged.append(prev)
                prev = interval
            else:
                prev[-1] = max(prev[-1], interval[-1])
        merged.append(prev)
        return merged
                