class Solution():
    def commonprefix(self, strs):
        if not strs:
            return ""
        common = ""
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != char:
                    return common
            common += char
        return common

if __name__ == "__main__":
    sol = Solution()
    print(sol.commonprefix(["flower","flow","flight"]))