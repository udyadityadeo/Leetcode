class Solution:
    def plusone(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
        return [1] + digits
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusone([1, 2, 3]))