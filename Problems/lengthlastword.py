class Solution:
    def lengthoflastword(self, s):
        i = len(s)-1
        length = 0

        while s[i] == ' ' and i >= 0:
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthoflastword("Hello World"))
    print(sol.lengthoflastword("   fly me   to   the moon  "))
    print(sol.lengthoflastword("luffy is still joyboy"))

