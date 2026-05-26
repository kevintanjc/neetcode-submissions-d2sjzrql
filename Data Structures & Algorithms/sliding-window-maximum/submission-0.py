class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lp = 0
        rp = k - 1
        output = []

        while rp < len(nums):
            output.append(max(nums[lp:rp + 1]))
            lp += 1
            rp += 1

        return output