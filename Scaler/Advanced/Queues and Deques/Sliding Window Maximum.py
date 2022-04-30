import collections

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        C = []
        dq = collections.deque()
        window_start = 0
        for window_end in range(len(A)):
            n = A[window_end]
            while dq and dq[-1] < n:
                dq.pop()
            if not dq or dq[-1] >= n:
                dq.append(n)
            if window_end - window_start + 1 == B:
                C.append(dq[0])
                if dq and dq[0] == A[window_start]:
                    dq.popleft()
                window_start += 1
        return C