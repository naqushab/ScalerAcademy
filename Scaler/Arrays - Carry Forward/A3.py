class Solution:
  # @param A : list of integers
  # @return an integer
  def bulbs(self, A):
    switches = 0
    for n in A:
        if switches%2 == 0:
            c_state = n
        else:
            c_state = 1-n
        if c_state == 0:
            switches += 1
    return switches