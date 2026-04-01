class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r - l) // 2 + l

            if nums[m + 1] < nums[m]:
                return nums[m + 1]

            elif nums[m] > nums[l] and nums[m] > nums[r]:
                #search right
                l = m + 1

            else:
                r = m

        return nums[l]
