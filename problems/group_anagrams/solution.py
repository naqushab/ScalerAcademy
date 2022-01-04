class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [strs]
        else:
            strs.sort(key=lambda x: sorted(x))
            print(strs)
            s, f = 0, 1
            ans = []
            bucket = [strs[0]]
            while f < len(strs):
                if sorted(strs[s]) != sorted(strs[f]):
                    ans.append(bucket)
                    bucket = []
                    s = f
                bucket.append(strs[f])
                f += 1
                if f == len(strs):
                    ans.append(bucket)
            return ans