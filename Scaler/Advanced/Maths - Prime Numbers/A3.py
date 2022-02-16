import collections

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = max(A)
        seive = [True] * (l + 1)
        seive[0] = seive[1] = False
        for i in range(2, int(l ** 0.5) + 1):
            if seive[i]:
                for j in range(i * i, l + 1, i):
                    seive[j] = False
        primes_before = [0] * (l + 1)
        # contribution technique - count the number of primes before each number
        for i in range(2, l + 1):
            if seive[i]:
                primes_before[i] = primes_before[i - 1] + 1
            else:
                primes_before[i] = primes_before[i - 1]
        # count the number of primes in each interval, eg [5 to 7) -> 5, 6, 7 -> 3, 3, 4
        # there is a asshole way to do this, but I don't care. You need to sort the input array and use two pointers
        # but since this is marked as 'Easy', I will use hashmap
        m = collections.defaultdict(lambda: 0)
        for i in A:
            if i == 1: # sneaky bastard
                continue
            m[primes_before[i]] += 1
        ans = 0
        mod = 10 ** 9 + 7
        for k, v in m.items():
            ans += (pow(2, v, mod)-1) % mod # contribution technique to find subsequences
            ans = ans % mod
        return ans
        


if __name__ == "__main__":
    s = Solution()
    A = [2, 3, 2, 3]
    print(s.solve(A))
    A = [2, 3, 4]
    print(s.solve(A))
    A = [4, 5, 6]
    print(s.solve(A))
