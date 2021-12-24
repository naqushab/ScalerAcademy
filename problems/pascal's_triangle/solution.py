class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1], [1, 1]]
        else:
            ans = [[1], [1, 1]]
            for i in range(3, n+1):
                row = [1]*i
                prev_row = ans[-1]
                for j in range(1, len(row)-1):
                    row[j] = prev_row[j-1] + prev_row[j]
                ans.append(row)
            return ans