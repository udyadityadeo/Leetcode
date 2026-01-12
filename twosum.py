class Solution:
    def twosum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in seen:
                return [seen[needed], i]
            seen[n] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twosum([2, 7, 11, 15], 9))