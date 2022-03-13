class UpdateHeavyAPIProcessor:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_num = len(matrix)
        self.col_num = len(matrix[0])

    def update(self, r, c, val):
        if 0 <= r < self.row_num and 0 <= c < self.col_num:
            self.matrix[r][c] = val
        return

    def query(self, r1, c1, r2, c2):
        if 0 <= r1 < self.row_num and 0 <= c1 < self.col_num and 0 <= r2 < self.row_num and 0 <= c2 < self.col_num:
            submatrix_sum = 0
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    submatrix_sum += self.matrix[i][j]
            return submatrix_sum
        else:
            return -1


class QueryHeavyAPIProcessor:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_num = len(matrix)
        self.col_num = len(matrix[0])
        self.prefix_sum_matrix = self._calc_prefix_sum(matrix)

    def _calc_prefix_sum(self, matrix):
        prefix_sum = [[0 for _ in range(self.col_num)] for _ in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                if i == 0 and j == 0:
                    prefix_sum[i][j] = matrix[i][j]
                elif i == 0:
                    prefix_sum[i][j] = prefix_sum[i][j-1] + matrix[i][j]
                elif j == 0:
                    prefix_sum[i][j] = prefix_sum[i-1][j] + matrix[i][j]
                else:
                    prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + matrix[i][j]
        return prefix_sum

    def update(self, r, c, val):
        self.matrix[r][c] = val
        for i in range(r, self.row_num):
            for j in range(c, self.col_num):
                if i == 0 and j == 0:
                    self.prefix_sum_matrix[i][j] = self.matrix[i][j]
                elif i == 0:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i][j-1] + self.matrix[i][j]
                elif j == 0:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i-1][j] + self.matrix[i][j]
                else:
                    self.prefix_sum_matrix[i][j] = self.prefix_sum_matrix[i-1][j] + self.prefix_sum_matrix[i][j-1] - self.prefix_sum_matrix[i-1][j-1] + self.matrix[i][j]
        return

    def query(self, r1, c1, r2, c2):
        if 0 <= r1 < self.row_num and 0 <= c1 < self.col_num and 0 <= r2 < self.row_num and 0 <= c2 < self.col_num:
            if r1 == 0 and c1 == 0:
                return self.prefix_sum_matrix[r2][c2]
            elif r1 == 0:
                return self.prefix_sum_matrix[r2][c2] - self.prefix_sum_matrix[r2][c1-1]
            elif c1 == 0:
                return self.prefix_sum_matrix[r2][c2] - self.prefix_sum_matrix[r1-1][c2]
            else:
                return self.prefix_sum_matrix[r2][c2] - self.prefix_sum_matrix[r1-1][c2] - self.prefix_sum_matrix[r2][c1-1] + self.prefix_sum_matrix[r1-1][c1-1]
        else:
            return -1


class EqualLoadAPIProcessor:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_num = len(matrix)
        self.col_num = len(matrix[0])
        self.prefix_sum_matrix = self._calc_prefix_sum(matrix)

    def _calc_prefix_sum(self, matrix):
        prefix_sum = [[0 for _ in range(self.col_num)] for _ in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                if j == 0:
                    prefix_sum[i][j] = matrix[i][j]
                else:
                    prefix_sum[i][j] = prefix_sum[i][j-1] + matrix[i][j]
        return prefix_sum

    def update(self, r, c, val):
        self.matrix[r][c] = val
        for i in range(c, self.col_num):
            if i == 0:
                self.prefix_sum_matrix[r][i] = self.matrix[r][i]
            else:
                self.prefix_sum_matrix[r][i] = self.prefix_sum_matrix[r][i-1] + self.matrix[r][i]
        return

    def query(self, r1, c1, r2, c2):
        sub_matrix_sum = 0
        if 0 <= r1 < self.row_num and 0 <= c1 < self.col_num and 0 <= r2 < self.row_num and 0 <= c2 < self.col_num:
            for r in range(r1, r2+1):
                if c1 == 0:
                    sub_matrix_sum += self.prefix_sum_matrix[r][c2]
                else:
                    sub_matrix_sum += self.prefix_sum_matrix[r][c2] - self.prefix_sum_matrix[r][c1-1]
            return sub_matrix_sum
        else:
            return -1

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    qhprocessor = QueryHeavyAPIProcessor(matrix)
    print(qhprocessor.query(0, 0, 2, 2))
    qhprocessor.update(0, 0, 0)
    print(qhprocessor.query(0, 0, 2, 2))
    qhprocessor.update(0, 0, 1)
    print(qhprocessor.query(0, 0, 2, 2))
    elprocessor = EqualLoadAPIProcessor(matrix)
    print(elprocessor.query(0, 0, 2, 2))
    elprocessor.update(0, 0, 0)
    print(elprocessor.query(0, 0, 2, 2))
    elprocessor.update(0, 0, 1)
    print(elprocessor.query(0, 0, 2, 2))
