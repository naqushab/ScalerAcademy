class Solution:
    # @param A : list of integers
    # @return an integer
    def subarray(self, idx):
        if len(idx) == 0:
            return 0
        count_0_subarray = 0
        count = 1
        for j in range(1, len(idx)):
            if idx[j] - idx[j-1] == 1:
                count += 1
            else:
                count_0_subarray += ((count*(count+1))//2)
                count = 1
        count_0_subarray += ((count*(count+1))//2)
        return count_0_subarray

    def solve(self, A):
        ans = 0
        n = len(A)
        subarray_count = (n*(n+1))//2
        maxl = len(bin(max(A))) - 2
        for i in range(maxl):
            mask = 1<<i
            index = []
            for j in range(n):
                if A[j] & mask == 0:
                    index.append(j)
            subarray_count_1 = subarray_count - self.subarray(index)
            ans += ((subarray_count_1) * mask)
        return ans % (10**9 + 7)

if __name__ == "__main__":
    s = Solution()
    print(s.solve(A=[ 1, 2, 3, 4, 5 ]))