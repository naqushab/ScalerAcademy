class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        l, r = max(C)*B, sum(C)*B
        ans = 0
        while l <= r:
            k = (l+r)//2
            if self.if_all_painted(A, B, C, k):
                ans = k
                r = k-1
            else:
                l = k+1
        return ans % 10000003

    def if_all_painted(self, A, B, C, k):
        number_of_worker = 1
        cur_time = 0
        for i in range(len(C)):
            if cur_time + (B*C[i]) <= k:
                cur_time += (B*C[i])
            elif number_of_worker < A:
                number_of_worker += 1
                cur_time = C[i]*B
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.paint(3, 10, [ 185, 186, 938, 558, 655, 461, 441, 234, 902, 681]))
    print(s.paint(2, 5, [1, 10]))
    print(s.paint(10, 1, [1, 8, 11, 3]))