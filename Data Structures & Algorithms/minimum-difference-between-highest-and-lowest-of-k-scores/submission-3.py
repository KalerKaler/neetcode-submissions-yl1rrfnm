class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:


        nums.sort()
        if k >= len(nums):
            return max(nums) - min(nums)

        l, r = 0, k
        minDiff = float('inf')

        while r <= len(nums):

            window = nums[l : r]
            minDiff = min(minDiff, max(window) - min(window))

            l += 1
            r += 1
        
        return minDiff

        