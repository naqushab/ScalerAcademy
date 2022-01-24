class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        self.ans = math.inf
        nums.sort()
        n = len(nums)
        
        def search(l, x):
            r = len(nums) -1
            a = math.inf
            while l<r:
                s = nums[l] + nums[r]
                if s == x:
                    a = s
                    break
                if s > x:
                    r -= 1
                    if abs(x-s) < abs(x-a):
                        a = s
                if s < x:
                    l += 1
                    if abs(x-s) < abs(x-a):
                        a = s
            return a

        # main program
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            s = search(i+1, target-nums[i])
            if abs(target - (s+nums[i])) < abs(target - self.ans):
                self.ans = s+nums[i]
        return self.ans