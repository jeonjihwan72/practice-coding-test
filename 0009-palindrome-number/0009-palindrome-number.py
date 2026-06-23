class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 숫자를 문자열로 변환
        num_string = str(x)

        start_index = 0
        end_index = len(num_string)-1
        
        is_palindrome = True

        while start_index < end_index:
            if num_string[start_index] != num_string[end_index]:
                is_palindrome = False
                break
            
            start_index += 1
            end_index -= 1
        
        return is_palindrome