class Solution:
    def addbinary(self, a , b):
        digita = 0
        digitb = 0
        i, j = 0, 0
        carry = 0
        result = ""
        while i >=0 or j>= 0:
            if i>=0:
                digita == 1 if a[i] == '1' else 0
            else:
                digita == 0

            if j >= 0:
                digitb == 1 if b[j] == '1' else 0
            else:
                digitb == 0

            if digita == 1 and digitb == 1:
                if carry == 1:
                    result += 1 
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addbinary("1010", "1011"))