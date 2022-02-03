'''
Q1. Add One To Number

Problem Description

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        c = 0
        ans = []
        pos = 0
        while A[pos] == 0:
          pos += 1
        for i in range(n-1, pos-1, -1):
          c = c + A[i]
          if i == n-1:
              c += 1
          d, c = c%10, c//10
          ans.insert(0, d)
        if c != 0:
          ans.insert(0, c)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne(A=[ 3, 0, 6, 4, 0 ]))
    print(s.plusOne(A=[ 9, 9, 9 ]))
    print(s.plusOne(A=[ 0, 0, 0, 9, 9, 9 ]))
    print(s.plusOne(A=[ 0, 0, 1, 0, 0 ]))