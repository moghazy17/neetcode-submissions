class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = [x[0] for x in c.most_common()]
        return ans[:k]