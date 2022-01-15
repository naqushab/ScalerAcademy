class Solution:
    def minJumps(self, arr: List[int]) -> int:
        m = collections.defaultdict(list)
        for i, n in enumerate(arr):
            m[n].append(i)
        visited = [False]*len(arr)
        q = collections.deque()
        visited[0] = True
        step = 0
        q.append(0)
        while q:
            ql = len(q)
            for _ in range(ql):
                point = q.popleft()
                if point == len(arr)-1:
                    return step
                for p in m[arr[point]]:
                    if not visited[p]:
                        visited[p] = True
                        q.append(p)
                del m[arr[point]]
                if point+1 < len(arr) and not visited[point+1]:
                    visited[point+1] = True
                    q.append(point+1)
                if point-1 >= 0 and not visited[point-1]:
                    visited[point-1] = True
                    q.append(point-1)
            step += 1