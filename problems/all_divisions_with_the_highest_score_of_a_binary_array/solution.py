class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros, ones = nums.count(0), nums.count(1)
        zeros_so_far, ones_so_far = 0, 0
        score = [0]*(n+1)
        score[0] = ones
        for i in range(n):
            if nums[i] == 0:
                zeros_so_far += 1
            else:
                ones_so_far += 1
            score[i+1] = zeros_so_far + (ones-ones_so_far)
        max_score = max(score)
        ans = []
        for i in range(n+1):
            if score[i] == max_score:
                ans.append(i)
        return ans