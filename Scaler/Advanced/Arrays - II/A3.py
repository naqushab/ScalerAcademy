class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        current_sum = 0
        l = 0
        while l < B:
            current_sum += A[l]
            l += 1
        ans = current_sum
        l -= 1
        r = n-1
        while r > n-B-1:
            current_sum -= A[l]
            l -= 1
            current_sum += A[r]
            r -= 1
            ans = max(ans, current_sum)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert 6253 == s.solve(A=[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5,
                            942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229,
                            538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 
                            141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ],
                            B=48)


# -533, -666, -500, 169, 724 -> 5 - 2