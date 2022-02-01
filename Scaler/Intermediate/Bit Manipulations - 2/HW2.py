class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mask = 1<<31
        temp_arr = A
        selection_arr = []
        mask = 1
        max_num = max(A)
        while max_num > 0:
            mask <<= 1
            max_num >>= 1
        while len(temp_arr) >= 4 and mask > 0:
            for n in temp_arr:
                if mask & n:
                    selection_arr.append(n)
            mask = mask>>1
            if len(selection_arr) >= 4:
                temp_arr = selection_arr
            selection_arr = []
        if len(temp_arr) >= 4:
            temp_arr.sort()
            return temp_arr[-1] & temp_arr[-2] & temp_arr[-3] & temp_arr[-4]
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    s.solve(A=[127, 1, 18, 15, 16, 7, 3, 83, 31, 23, 31])