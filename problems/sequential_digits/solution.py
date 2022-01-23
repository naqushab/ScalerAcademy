class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = collections.deque()
        for i in range(1, 10):
            q.append(i)
        ans = []
        while q:
            num = q.popleft()
            if low<=num<=high:
                ans.append(num)
            if num > high:
                return ans
            if num % 10 != 9:
                new_num = num * 10 + (num % 10) + 1
                q.append(new_num)
        return ans