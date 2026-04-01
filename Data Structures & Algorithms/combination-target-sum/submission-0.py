class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, path, total):
            if total == target:
                valid = path.copy()
                result.append(valid)
                return

            if total > target or i > len(nums) - 1:
                return

            # take
            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()

            # do not take
            dfs(i + 1, path, total)

        dfs(0, [], 0)
    
        return result


