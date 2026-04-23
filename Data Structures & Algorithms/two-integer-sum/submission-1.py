class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):

            x = target - nums[i]

            if x in dic:
                return [dic[x], i]
            
            dic[nums[i]] = i
        
        return

