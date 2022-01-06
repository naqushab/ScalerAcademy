class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            temp = [1]*(i+1)
            for j in range(0, i-1):
                temp[j+1] = ans[-1][j] + ans[-1][j+1]
            ans.append(temp)
        return ans[rowIndex]