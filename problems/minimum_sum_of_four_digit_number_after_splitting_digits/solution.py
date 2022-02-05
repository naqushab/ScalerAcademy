class Solution:
    def minimumSum(self, num: int) -> int:
        ns = list(str(num))
        ns.sort()
        one = ns[0] + ns[3]
        two = ns[1] + ns[2]
        return int(one) + int(two)