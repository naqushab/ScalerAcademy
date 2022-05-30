import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        coins = 0
        while A > 0:
            num_coin = math.floor(math.log(A, 5))
            A -= (5**num_coin)
            coins += 1
        return coins

if __name__ == "__main__":
    print(Solution().solve(47))

'''
5^x = y
'''