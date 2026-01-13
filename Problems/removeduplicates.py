class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)
    
if __name__ == "__main__":
    sol = Solution()
    inputs = [2, 2, 2, 3, 3, 4, 5]
    print(sol.removeDuplicates(inputs))