class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            hand = target - n
            if hand in seen:
                return [seen[hand], i]
            seen[n] = i