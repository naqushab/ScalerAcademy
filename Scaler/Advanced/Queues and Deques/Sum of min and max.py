import collections

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_q = collections.deque()
        min_q = collections.deque()
        ans = 0
        window_start = 0
        for window_end in range(len(A)):
            n = A[window_end]
            while max_q and n > max_q[-1]:
                max_q.pop()
            while min_q and n < min_q[-1]:
                min_q.pop()
            if not max_q or max_q[-1] >= n:
                max_q.append(n)
            if not min_q or min_q[-1] <= n:
                min_q.append(n)
            if window_end - window_start + 1 == B:
                ans += (max_q[0] + min_q[0]) % ((10**9) + 7)
                if A[window_start] == max_q[0]:
                    max_q.popleft()
                if A[window_start] == min_q[0]:
                    min_q.popleft()
                window_start += 1
        return ans % ((10**9) + 7)

if __name__ == '__main__':
    A = [2, 5, -1, 7, -3, -1, -2]
    B = 4
    print(Solution().solve(A, B))