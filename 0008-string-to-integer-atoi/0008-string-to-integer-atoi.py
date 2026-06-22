class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # 입력받은 문자열의 왼쪽 여백 제거        
        temp_s = s.lstrip()

        if temp_s == "":
            return 0

        negative_signed = False

        if temp_s[0] == '-':
            negative_signed = True
            temp_s = temp_s[1:]
        elif temp_s[0] == '+':
            temp_s = temp_s[1:]

        num_s = ""

        for char in temp_s:
            if 48 <= ord(char) <= 57:
                num_s += char
            else:
                break

        if num_s == "":
            return 0

        num = int(num_s)

        if negative_signed:
            num *= -1
        
        if num >= 2**31 - 1:
            return 2**31 -1
        
        if num <= -2**31:
            return -2**31

        return num