class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        m = bisect.bisect_left(arr, x)
        l = m-1
        r = m
        while k > 0 and l >= 0 and r < len(arr):
            if abs(arr[l]-x) <= abs(arr[r]-x):
                ans.insert(0, arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
            k -= 1
        while k > 0 and l >=0:
            ans.insert(0, arr[l])
            l -= 1
            k -= 1
        while k > 0 and r < len(arr):
            ans.append(arr[r])
            r += 1
            k -= 1
        return ans