class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        binary = ''
        while A:
            binary += str(A%2)
            A //= 2
        rev = binary + '0'*(32-len(binary))
        power = 0
        index = len(rev) -1
        ans = 0
        while index >= 0:
            ans += pow(2, power) * int(rev[index])
            index -= 1
            power += 1
        return ans