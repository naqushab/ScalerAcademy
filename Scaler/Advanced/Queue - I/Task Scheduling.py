import collections

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        time = 0
        q = collections.deque(A)
        for n in B:
            while q and q[0] != n:
                time += 1
                qf = q.popleft()
                q.append(qf)
            else:
                time += 1
                q.popleft()
        return time

if __name__ == '__main__':
    A = [ 6, 7, 1, 2, 4, 5, 8, 3 ]
    B = [ 3, 7, 2, 5, 1, 8, 4, 6 ]
    print(Solution().solve(A, B))