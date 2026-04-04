from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        @cache
        def dp(i, total):
            if i + 2 >= len(nums):
                best = max(nums[i], nums[i+1] if i + 1 < len(nums) else 0)
                return total + best

            # choice 1: rob house
            output = dp(i + 2, total + nums[i])

            # choice 2: dont rob house
            output = max(output, dp(i + 1, total))
            
            return output

        return dp(0, 0)
