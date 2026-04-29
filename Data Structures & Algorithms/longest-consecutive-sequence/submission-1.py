class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort() 
        s = 1
        m = 0

        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff < 2:
                s = s + diff
            else:

                m = max(m,s)
                s = 0

        return max(m,s)


