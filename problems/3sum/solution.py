class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def find_triplet(target, end):
            s, e = 0, end-1
            if e-s+1 < 2:
                return
            while s<e:
                sm = nums[s] + nums[e]
                if sm == target:
                    t = [nums[s], nums[e], nums[end]]
                    ans.append(t)
                    while 0 <= s < len(nums)-1 and nums[s] == nums[s+1]:
                        s += 1
                    else:
                        s += 1
                    while 1 <= e <= len(nums)-1 and nums[e] == nums[e-1]:
                        e -= 1
                    else:
                        e -= 1
                elif sm > target:
                    e -= 1
                else:
                    s += 1
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                continue
            find_triplet(-nums[i], i)
        return ans