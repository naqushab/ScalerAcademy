'''
Q1. Maximum Absolute Difference

Problem Description

You are given an array of N integers, A1, A2, …. AN.

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
      s, d = [], []
      for i, n in enumerate(A):
        s.append(n+i)
        d.append(n-i)
      maxs, mins = max(s), min(s)
      maxd, mind = max(d), min(d)
      return maxs-mins if maxs-mins > maxd-mind else maxd-mind


if __name__ == "__main__":
    s = Solution()
    print(s.maxArr(A=[ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ])) #167