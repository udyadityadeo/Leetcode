def two_sum():
    nums= int(input("input array:").split())
    target = int(input("input target:"))

    for i in range(len(nums)):
        y = target - nums[i]
        if y in nums[i + 1:]:
            return nums[i, i+1]
        
two_sum()

def palindrome():
    s = int(input("input number:"))
    rev = 0
    temp = s
    while s > 0:
        digit = s % 10
        rev = rev * 10 + digit
        s = s // 10
    if temp == rev:
        return True
    else:
        return False
    
def roman_to_integer():
    roman = input("input roman numeral:")
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman):
        curr_value = roman_dict.get(char, 0)
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total

def longest_common_prefix():
    strs = input("Input strings (space-separated): ").split()
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
