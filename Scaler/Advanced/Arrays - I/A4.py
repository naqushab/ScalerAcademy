'''
Q4. Beggars Outside Temple

There are N (N > 0) beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to his faith and ability) to some K beggars sitting next to each other.

Given the amount donated by each devotee to the beggars ranging from i to j index, where 1 <= i <= j <= N, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = [0] * A
        for beg, end, amount in B:
          ans[beg-1] += amount
          if end-1 != A-1:
            ans[end] -= amount
        for i in range(A):
          if i == 0:
            pass
          else:
            ans[i] = ans[i] + ans[i-1]
        return ans
