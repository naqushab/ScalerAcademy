import bisect

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.merge_sort(A) % (10**9 + 7)
    
    def merge_sort(self, A):
        # return inversion count of array A
        if len(A) <= 1:
            return 0
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        l_inv = self.merge_sort(left)
        r_inv = self.merge_sort(right)
        merged_inv = self.merge(A, left, right)
        return l_inv + r_inv + merged_inv

    def merge(self, A, left, right):
        # merge two sorted arrays
        i, j, k = 0, 0, 0
        count = 0
        while i < len(left) and j < len(right):
            if left[i] > 2*right[j]:
                count += len(left) - i
                j += 1
            else:
                i += 1
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return count


if __name__ == '__main__':
    s = Solution()
    A = [ 769, -71, 599, -1438, -530, -512, 1680, 1907, -301, 492, -844, 1765, -188, 685, -1879, -699, -990, 1022, 459, 528, -930, 1051, 1412, -1598, 245, -480, 1979, 1212, 1177, 447, -509, 881, 1968, -1603, -429, 1165, 405, 426, -1610, 931, -835, -1156, 1273, -143, -940, 199, -1886, -1646, 390, -1349, -256, -256, -103, -135, 637, -605, 55, -1805, -17, -229, 1162, 288, -818, -922, 32, -1032, -1823, -1874, -1650, 146, 721, 1586, 1969, 1720, -993, -1137, -1233, -1629, -879, -277, 444, -1191, -1273, 127, 1785, 1407, -1460, 414, -1578, -1348, 72, -794, 632, 877, 338, 1921, -650, -1314, 1187, -40 ]
    print(s.solve(A)) # 2761