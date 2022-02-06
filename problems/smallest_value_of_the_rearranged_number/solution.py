class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num *= -1
            ans = list(str(num))
            ans.sort(reverse=True)
            ans = ''.join(ans)
            ans = int(ans) * -1
            return ans
        elif num == 0:
            return 0
        else:
            ans = list(str(num))
            ans.sort()
            i = 0
            while ans[i] == '0':
                i+=1
            ans[0], ans[i] = ans[i], ans[0]
            ans = ''.join(ans)
            return int(ans)