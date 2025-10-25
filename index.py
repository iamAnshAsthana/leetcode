class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []

solver = Solution()
print(f"Output: {solver.twoSum([11, 12, 1, 2], 3)}")


