class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        original = x

        while x > 0:
            l = x % 10
            rev = rev*10 + l
            x = x // 10
        
        return rev == original

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(10))
