class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        ### 포인터를 양쪽 끝에서부터 접근시키는 방법
        # # 숫자를 문자열로 변환
        # num_string = str(x)

        # start_index = 0
        # end_index = len(num_string)-1
        
        # is_palindrome = True

        # while start_index < end_index:
        #     if num_string[start_index] != num_string[end_index]:
        #         is_palindrome = False
        #         break
            
        #     start_index += 1
        #     end_index -= 1
        
        # return is_palindrome

        # 문자열 자체를 뒤집어 비교하는 방법
        num_string = str(x)
        reverse_x = num_string[::-1]

        if num_string == reverse_x: return True
        else: return False

        