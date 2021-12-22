class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        merged_interval = []
        for interval in intervals:
            if merged_interval == []:
                merged_interval = interval
            else:
                if interval[0] > merged_interval[-1]:
                    ans.append(merged_interval)
                    merged_interval = interval
                else:
                    merged_interval = [merged_interval[0], max(merged_interval[-1] ,interval[-1])]
        ans.append(merged_interval)
        return ans