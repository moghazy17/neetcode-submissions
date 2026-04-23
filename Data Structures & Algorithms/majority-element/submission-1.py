class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1

        for n in nums:

            if n == candidate:
                counter += 1
            elif counter == 0:
                candidate = n 
                counter = 1
            else:
                counter -= 1

        return candidate