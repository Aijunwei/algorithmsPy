class Solution:
    def twoSum(self, nums, target):
        hash_map = dict()
        for i, val in enumerate(nums):
            if target - val in hash_map:
                return [i, hash_map[target-val]]
            hash_map[val] = i

solution = Solution()
print(solution.twoSum([1,2,3,4,5,56], 6))