class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols_value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = 0
        previous_symbol_value = 0

        for symbol in reversed(s):
            current_symbol_value = symbols_value[symbol]

            if current_symbol_value >= previous_symbol_value:
                result += current_symbol_value
            else:
                result -= current_symbol_value
            
            previous_symbol_value = current_symbol_value
        
        return result