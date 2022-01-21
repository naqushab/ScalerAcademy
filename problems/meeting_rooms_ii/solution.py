class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        st = sorted([x[0] for x in intervals])
        et = sorted([x[1] for x in intervals])
        i, j = 0, 0
        ans = count = 0
        n = len(intervals)
        while i < n:
            if st[i] < et[j]:
                i += 1
                count  += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans