class Solution:
    def isValid(self, s):
        map = {")": "(","}": "{", "]":"["}

        stack = []
        for char in s:
            if char in map.values():
                stack.append(char)

            elif char in map:
                if not stack or map[char] != stack.pop():
                    return False
            return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("{[(]}"))    
        
