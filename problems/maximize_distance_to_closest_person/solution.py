class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = -1
        ans = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if l == -1:
                    ans = i
                else:
                    ans = max(ans, (i-l)//2)
                l = i
            elif i == len(seats)-1 and seats[i] == 0:
                ans = max(ans, i-l)
        return ans