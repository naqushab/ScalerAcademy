class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_arr_i = cur_arr_i = 0
        n = len(nums)
        while cur_arr_i < n:
            while cur_arr_i < n and nums[cur_arr_i] == val:
                cur_arr_i += 1
            else:
                if cur_arr_i < n:
                    nums[new_arr_i] = nums[cur_arr_i]
                    new_arr_i += 1
                    cur_arr_i += 1
        return new_arr_i