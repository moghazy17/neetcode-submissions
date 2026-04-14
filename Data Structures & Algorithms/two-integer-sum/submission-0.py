class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for k,v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v],k]
            dic[v] = k