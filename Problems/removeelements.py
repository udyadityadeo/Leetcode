class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1       
        return k

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3)) 