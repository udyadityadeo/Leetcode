class Solution:
    def Irtoi(self, s):

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
        l = len(s) - 1
        total = 0
        prev = 0
        for i in range(l, -1, -1):
            current = roman[s[i]]
            if current < prev:
                total -= current
            else:
                total +=current
            
            prev = current
        return total
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.Irtoi('XIV'))
