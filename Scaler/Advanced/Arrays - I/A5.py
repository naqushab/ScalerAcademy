'''
Q5. Flip
Problem Description

You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, …, AN. 
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, …, AR. 
By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. 
Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, 
return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
'''

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
      n = len(A)
      arr = [1]*n
      for i in range(n):
        if A[i] == '1':
          arr[i] = -1
      max_sum = float('-inf')
      current_sum = 0
      global_start, global_end = 0, 0
      start, end = 0, 0
      for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
          end = i
          max_sum = current_sum
          global_start = start
          global_end = end
        if current_sum < 0:
          start = i + 1
          current_sum = 0
      if global_start == global_end and arr[global_start] == -1:
        return []
      return [global_start+1, global_end+1]

if __name__ == "__main__":
    s = Solution()
    print(s.flip(A="1101"))
    print(s.flip(A="1"))
    print(s.flip(A="111111111"))
    print(s.flip(A="0101100001"))
    print(s.flip(A="01111"))
    print(s.flip(A="010"))
    print(s.flip(A="010000011"))
