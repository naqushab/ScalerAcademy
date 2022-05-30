class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        ans = []

        mapping = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def recurse(cur_str, index):
            if index == len(A):
                ans.append(''.join(cur_str[:]))
                return
            for ch in mapping[A[index]]:
                cur_str.append(ch)
                recurse(cur_str, index+1)
                cur_str.pop()

        recurse([], 0)

        return ans