class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        r = len(bank)
        if r == 0:
            return 0
        prev_count = 0
        ans = 0
        for s in bank:
            count_cam = s.count('1')
            if count_cam > 0:
                if prev_count > 0:
                    ans += count_cam*prev_count
                prev_count = count_cam
        return ans