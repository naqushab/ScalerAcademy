class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        c = 0
        for i in range(n):
            while i != A[i]:
                temp = A[A[i]]
                A[A[i]] = A[i]
                A[i] = temp
                c += 1
        return c

if __name__ == "__main__":
    s = Solution()
    A = [0, 1, 2, 3, 4]
    print(s.solve(A)) # 0
    A = [1, 2, 3, 4, 0]
    print(s.solve(A)) # 4
    A = [2, 0, 1, 3]
    print(s.solve(A)) # 2
    A = [0, 4, 3, 1, 2, 5]
    print(s.solve(A)) # 3
    A = [ 6, 50, 16, 30, 37, 12, 43, 52, 24, 2, 53, 28, 31, 36, 10, 32, 51, 60, 64, 38, 3, 46, 7, 4, 55, 72, 75, 66, 73, 68, 54, 22, 25, 65, 5, 49, 0, 8, 47, 78, 35, 57, 83, 90, 27, 9, 19, 26, 76, 41, 39, 40, 1, 11, 67, 61, 71, 56, 58, 108, 110, 102, 15, 70, 59, 14, 42, 23, 29, 20, 118, 13, 106, 17, 69, 18, 21, 34, 44, 62, 33, 80, 45, 87, 48, 63, 74, 131, 134, 111, 77, 79, 81, 139, 132, 124, 82, 84, 85, 86, 88, 89, 91, 92, 93, 130, 94, 98, 95, 96, 151, 97, 99, 100, 109, 101, 142, 103, 143, 104, 105, 146, 107, 112, 113, 138, 114, 115, 116, 117, 160, 119, 120, 148, 145, 121, 122, 123, 125, 126, 127, 135, 128, 153, 129, 133, 144, 136, 137, 140, 141, 147, 149, 150, 152, 154, 155, 156, 157, 158, 159 ]
    print(s.solve(A)) # 154