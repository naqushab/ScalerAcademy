class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        non_overlapping_interval = 0
        intervals.sort(key = lambda x: x[0])
        prev_end = intervals[0][-1]
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if prev_end <= cur_interval[0]:
                prev_end = cur_interval[-1]
            else:
                non_overlapping_interval += 1
                prev_end = min(prev_end, cur_interval[-1])
        return non_overlapping_interval