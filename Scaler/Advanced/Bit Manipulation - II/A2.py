class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        max_power_of2_inrange = 0
        while 1 << max_power_of2_inrange < A:
            max_power_of2_inrange += 1
        max_power_of2_inrange -= 1
        before_max_power_of2_inrange = ((1<<(max_power_of2_inrange-1)) * max_power_of2_inrange)
        ones_after_max_power_of2_inrange = (A + 1 - (1<<max_power_of2_inrange))
        rem = A - (1<<max_power_of2_inrange)
        return before_max_power_of2_inrange + ones_after_max_power_of2_inrange + self.solve(rem)
    
    def simple(self, A):
        ans = 0
        l = len(bin(A)) - 2
        for i in range(l):
            for num in range(A+1):
                mask = 1 << i
                if num & mask:
                    ans += 1
        return ans % ((10**9)+7)

    def dp(self, A):
        dp = [0] * (A+1)
        dp[1] = 1

        for i in range(2, A + 1):
            num = i>>1
            if i & 1:
                dp[i] = dp[num] + 1
            else:
                dp[i] = dp[num]
        return sum(dp[1:])


if __name__ == "__main__":
    s = Solution()
    A = 11
    print(s.solve(A))