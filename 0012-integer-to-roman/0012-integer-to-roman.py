class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousand_string = ""
        hundred_string = ""
        ten_string = ""
        one_string = ""

        thousand = num // 1000
        hundred = (num % 1000) // 100
        ten = (num % 100) // 10
        one = num % 10

        # 1,000 단위 로마 변환
        thousand_string = "M" * thousand

        # 100 단위 로마 변환
        if hundred > 8 :
            hundred_string = ("C" * (10-hundred)) + "M"
        elif hundred <= 8 and hundred >= 5:
            hundred_string = "D" + ("C" * (hundred-5))
        elif hundred < 5 and hundred > 3:
            hundred_string = ("C" * (5-hundred)) + "D"
        else:
            hundred_string = "C" * hundred
        
        # 10 단위 로마 변환
        if ten > 8 :
            ten_string = ("X" * (10-ten)) + "C"
        elif ten <= 8 and ten >= 5:
            ten_string = "L" + ("X" * (ten-5))
        elif ten < 5 and ten > 3:
            ten_string = ("X" * (5-ten)) + "L"
        else:
            ten_string = "X" * ten

        # 1 단위 로마 변환
        if one > 8 :
            one_string = ("I" * (10-one)) + "X"
        elif one <= 8 and one >= 5:
            one_string = "V" + ("I" * (one-5))
        elif one < 5 and one > 3:
            one_string = ("I" * (5-one)) + "V"
        else:
            one_string = "I" * one
        
        return thousand_string + hundred_string + ten_string + one_string