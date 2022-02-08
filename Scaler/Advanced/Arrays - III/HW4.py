class Solution:
	# @param A : integer
	# @return a list of list of integers
    def generateMatrix(self, A):
        left, right, top, bottom, count = False, True, False, False, A**2
        ans = [[0]*A for _ in range(A)]
        ans[0][0] = 1
        i = 2
        r, c = 0, 0
        while i <= count:
            if right:
                c += 1
                while c<A and ans[r][c] == 0:
                    ans[r][c] = i
                    i += 1
                    c += 1
                right = False
                bottom = True
                c -= 1
            if bottom:
                r += 1
                while r<A and ans[r][c] == 0:
                    ans[r][c] = i
                    i += 1
                    r += 1
                bottom = False
                left = True
                r -= 1
            if left:
                c -= 1
                while c>=0 and ans[r][c] == 0:
                    ans[r][c] = i
                    i += 1
                    c -= 1
                left = False
                top = True
                c += 1
            if top:
                r -= 1
                while r>=0 and ans[r][c] == 0:
                    ans[r][c] = i
                    i += 1
                    r -= 1
                top = False
                right = True
                r += 1
        return ans