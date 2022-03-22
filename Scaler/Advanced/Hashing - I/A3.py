class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        running_sum = 0
        m = set()
        m.add(0)
        for n in A:
            running_sum += n
            if running_sum in m:
                return 1
            else:
                m.add(running_sum)
        return 0