class Solution:

  def rotate(self, nums: List[int], k: int) -> None:
    """Do not return anything, modify nums in-place instead."""
    n = len(nums)
    if n == 0:
      return

    k %= n  
    nums[:] = nums[n - k :] + nums[: n - k]