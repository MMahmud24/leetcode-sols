class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        n = len(nums)

        dp = [0] * n

        for i in range(n):
            if dp[i] > 1:
                continue

            if dp[i] == 0:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    dp[i] = 1
                else:
                    continue
                
                for j in range(i+1,n):
                    if nums[j] % 2 != nums[j-1] % 2 and nums[j] <= threshold:
                        dp[j] = dp[j-1] + 1
                    else:
                        break

        return max(dp)
        

    
