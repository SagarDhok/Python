

# First Missing Positive.
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

sol = Solution()
print(sol.firstMissingPositive([1, 2, 0]))         
print(sol.firstMissingPositive([3, 4, -1, 1]))     
print(sol.firstMissingPositive([7, 8, 9, 11, 12]))