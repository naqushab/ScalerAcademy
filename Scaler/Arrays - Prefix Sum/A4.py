class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        ps = [0]*len(A)
        ps[0] = A[0]
        
        for i in range(1, len(A)):
            ps[i] = ps[i-1] + A[i]
        
        ans = []
        for rng in B:
            l, r = rng[0], rng[1]
            l = l-1
            r = r-1
            if l == 0:
                ans.append(ps[r])
            else:
                ans.append(ps[r] - ps[l-1])
        return ans