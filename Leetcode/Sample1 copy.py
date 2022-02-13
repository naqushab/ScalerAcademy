import math
class Solution:
    def minimumRemoval(self, beans) -> int:
        n = len(beans)
        ans = math.inf
        for i in range(n):
            A = [beans[i]]*n
            c = 0
            for j in range(n):
                if A[j] > beans[j]:
                    c = math.inf
                    break
                else:
                    c += beans[j]-A[j]
            ans = min(ans, c)
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,6,5]
    print(s.minimumRemoval(nums))