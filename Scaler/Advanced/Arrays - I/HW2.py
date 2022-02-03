'''
Q2. Max Non Negative SubArray

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
      n = len(A)
      i = 0
      ans = []
      temp_ans = []
      sum, prev_sum = 0, 0
      while i < n:
        if A[i] >= 0:
          sum += A[i]
          temp_ans.append(A[i])
        if A[i] < 0 or (i == n-1 and A[i] > 0):
          if sum > prev_sum:
            ans = temp_ans
            prev_sum = sum
          elif sum == prev_sum:
            if len(temp_ans) > len(ans):
              ans = temp_ans
          temp_ans = []
          sum = 0
        i += 1
      return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxset(A=[1, 2, 5, -7, 2, 3]))
    print(s.maxset(A=[1, 2, 5, -7, -2, 18]))
    print(s.maxset(A=[ 24115, -75629, -46517, 30105, 19451, -82188, 99505, 6752, -36716, 54438, -51501, 83871, 11137, -53177, 22294, -21609, -59745, 53635, -98142, 27968, -260, 41594, 16395, 19113, 71006, -97942, 42082, -30767, 85695, -73671 ]))