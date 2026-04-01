class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            
            # if left is at most as big as middle, then the left side is sorted in order
            if nums[l] <= nums[m]:
                # if target lies between left and middle check left subarray
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # check right subarray
                else:
                    l = m + 1
            # if left is bigger than middle, right side is sorted in order
            else:
                # if target lies on right, search right subarray
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return l if l < len(nums) and nums[l] == target else -1