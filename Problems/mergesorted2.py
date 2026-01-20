class Solution:
    def merge(self, num1, m, num2, n):
        p1 = m - 1
        p2 = n-1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if num1[p1] >= num2[p2]:
                num1[p] = num1[p1]
                p1 -= 1

            else:
                num1[p] = num2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in num2, copy them
        while p2 >= 0:
            num1[p] = num2[p2]
            p2 -= 1
            p -= 1

if __name__ == "__main__":
    sol = Solution()
    num1 = [1, 2, 3, 0, 0, 0]
    m = 3
    num2 = [2, 5, 6]
    n = 3
    sol.merge(num1, m, num2, n)
    print(num1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge(num1, m, num2, n))
    num1 = [1, 2, 3, 0, 0, 0]
    m = 3
    num2 = [2, 5, 6]
    n = 3
    sol.merge(num1, m, num2, n)
    print(num1)