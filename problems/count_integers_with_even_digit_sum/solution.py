class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(n):
            s = str(n)
            add = 0
            for i in s:
                add += int(i)
            return add%2==0
        ans = 0
        for i in range(2, num+1):
            if digit_sum(i):
                ans += 1
        return ans