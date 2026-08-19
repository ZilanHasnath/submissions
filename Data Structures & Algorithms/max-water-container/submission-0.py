from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            distance = right - left
            current_water = distance * min(heights[left],heights[right])
            
            max_water = max(max_water, current_water)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_water