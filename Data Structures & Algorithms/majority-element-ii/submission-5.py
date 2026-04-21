class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        candidate1 = nums[0]
        candidate2 = 0
        count1 = 1
        count2 = 0
        s = len(nums)
        for n in nums:
            
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:   
                count1 -= 1
                count2 -= 1


        count1 = 0
        count2 = 0
        for n in nums:
            if n == candidate1:
                count1 = count1+1

            if n == candidate2:
                count2 = count2+1

        ans = []
        if count1 > s/3:
            ans.append(candidate1)

        if count2 > s/3:
            ans.append(candidate2)

        return ans

        


                
