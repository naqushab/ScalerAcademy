import math
# rank = number of characters less than first character * (N-1)! + rank of permutation of string with the first character removed


class Solution:
    def char_before(self, S, ch):
        sortS = sorted(S)
        count = 0
        for c in sortS:
            if c == ch:
                return count
            count += 1

    # @param A : string
    # @return an integer
    def findRank(self, A):
        # find the lexicographic rank of the string
        n = len(A)
        rank = 1
        for i in range(n):
            place = self.char_before(A[i:], A[i])
            if place > 0:
                rank += (math.factorial(n-i-1))*(place)
        return rank % 1000003
        

if __name__ == "__main__":
    s = Solution()
    A = "view"
    print(s.findRank(A))
    A = "acb"
    print(s.findRank(A))
    A = "a"
    print(s.findRank(A))
    A = "szt"
    print(s.findRank(A))