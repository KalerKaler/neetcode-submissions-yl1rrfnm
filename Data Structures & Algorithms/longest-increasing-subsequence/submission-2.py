class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # Standard Dynamic Programming approach for Longest Increasing Subsequence
        # The previous pointer approach was insufficient because LIS elements 
        # are not necessarily adjacent or at the ends of the array.
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)