'''
Q2. Rain Water Trapped

Problem Description

Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
  def trap(self, A):
        n = len(A)
        lgt = [0]*n
        rgt = [0]*n
        prev_lgt, prev_rgt = 0, 0
        for i in range(n):
            if i == 0:
                lgt[i] = 0
            else:
                lgt[i] = prev_lgt
            prev_lgt = max(prev_lgt, A[i])
        for i in range(n-1, -1, -1):
            if i == n-1:
                rgt[i] = 0
            else:
                rgt[i] = prev_rgt
            prev_rgt = max(prev_rgt, A[i])
        water = [0]*n
        for i in range(n):
            water[i] = min(lgt[i], rgt[i]) - A[i]
            if water[i] < 0:
                water[i] =0
        return sum(water)

if __name__ == "__main__":
    s = Solution()
    print(s.trap(A=[ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]))