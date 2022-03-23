'''
Problem Description
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

NOTE: The answer may be large so return the answer modulo (109 + 7).



Problem Constraints
1 <= N <= 105

0 <= A[i], B[i] <= 109



Input Format
The first argument given is an integer array A.
The second argument given is the integer array B.



Output Format
Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).



Example Input
Input 1:

 A = [1, 1, 2]
 B = [1, 2, 1]
Input 2:

 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]


Example Output
Output 1:

 1
Output 2:

 6
'''
import collections


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        x_map = collections.Counter(A)
        y_map = collections.Counter(B)
        count = 0
        for i in range(len(A)):
            m = x_map[A[i]] - 1
            n = y_map[B[i]] - 1
            count += m * n
        return count % (10**9 + 7)
