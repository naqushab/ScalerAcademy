'''
Problem Description
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.

Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.



Problem Constraints
1 <= N <= 2000
0 <= A[i], B[i] <= 109



Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.



Output Format
Return the number of unordered quadruplets that form a rectangle.



Example Input
Input 1:

 A = [1, 1, 2, 2]
 B = [1, 2, 1, 2]
Input 1:

 A = [1, 1, 2, 2, 3, 3]
 B = [1, 2, 1, 2, 1, 2]


Example Output
Output 1:

 1
Output 2:

 3
'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        points = []
        lookup = set()
        for i in range(len(A)):
            lookup.add((A[i], B[i]))
            points.append((A[i], B[i]))
        count = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    count += 1
        return count//2

if __name__ == '__main__':
    A = [1, 1, 2, 2]
    B = [1, 2, 1, 2]
    print(Solution().solve(A, B))
