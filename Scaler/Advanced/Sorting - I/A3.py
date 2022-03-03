class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_elem = min(A)
        max_elem = max(A)
        # 3 4
        # 1 2
        # 1 2 3 4
        sum_less_than_min = ((min_elem-1)*(min_elem))//2
        sum_till_max = (max_elem*(max_elem+1))//2
        expected_sum = sum_till_max - sum_less_than_min
        actual_sum = 0
        for n in A:
            actual_sum += n
        return 1 if actual_sum == expected_sum else 0