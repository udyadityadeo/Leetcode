class Solution:
    def addbinary(self, a , b):
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = ""

        while i >=0 or j>= 0 or carry:
            if i>=0:
                digita = 1 if a[i] == '1' else 0
            else:
                digita = 0

            if j >= 0:
                digitb = 1 if b[j] == '1' else 0
            else:
                digitb = 0

            '''Cases'''

            if digita == 1 and digitb == 1:
                if carry == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = 1

            elif digita == 0 and digitb == 0:
                if carry == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = 0
            
            else:
                if carry ==1:
                    result = '1' + result
                    carry = 1
                else:
                    result = '1' + result
                    carry = 0

            
            i -=1
            j -=1
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addbinary("1010", "1011"))
    print(sol.addbinary("111", "1"))