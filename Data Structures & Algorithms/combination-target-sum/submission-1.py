class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(i, path, total):
            if total == target:
                results.append(path)
                return

            if total > target or i > len(nums) - 1:
                return

            # choice 1: to take
            new_path = path.copy()
            new_path.append(nums[i])
            dfs(i, new_path, total + nums[i])

            # choice 2: to skip
            dfs(i + 1, path, total)

        dfs(0, [], 0)

        return results