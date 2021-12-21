# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1
        return l