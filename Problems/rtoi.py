class Solution:
    def rtoi(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
        total = 0
        prev_value = 0
        for char in reversed(s):
            current = roman[char]
            if current < prev_value:
                total -= current
            else:
                total += current
            
            prev_value = current
        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.rtoi("XIV"))