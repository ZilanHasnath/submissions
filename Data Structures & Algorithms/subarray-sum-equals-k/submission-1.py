class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
                
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count