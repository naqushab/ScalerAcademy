class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        merged = [intervals[0]]
        m = merged[-1]
        for interval in intervals[1:]:
            if interval[0] >= m[0] and interval[1] <= m[1]:
                continue
            else:
                merged.append(interval)
                m = merged[-1]
        return len(merged)
                