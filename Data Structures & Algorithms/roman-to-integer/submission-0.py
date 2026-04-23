class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        nums = []

        for c in s:
            nums.append(dic[c])

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                nums[i+1] -= nums[i]
                nums[i] = 0

        return sum(nums) 

