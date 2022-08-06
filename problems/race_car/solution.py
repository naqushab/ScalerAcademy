class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        q.append((0, 0, 1)) # m, p, v
        while q:
            m, p, v = q.popleft()
            if p == target:
                return m
            q.append((m+1, p+v, 2*v))
            if (p+v > target and v > 0) or (p+v < target and v < 0):
                q.append((m+1, p, -v/abs(v)))