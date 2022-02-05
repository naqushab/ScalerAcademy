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