class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_length = 0       # 미중복 문자열 최대 길이
        s_length = len(s)   # 문자열 길이

        for seperate in range(0, s_length):
            character_stack = []    # 등장한 문자 저장 스택 초기화
                                    # 반복마다 스택 초기화
            temp_length = 0  # 미중복 문자열 길이
                
            for point in range(seperate, s_length):
                character = s[point]
                if character in character_stack:    
                    # 문자열 중복을 탐지하는 경우
                    break
                
                character_stack.append(character)   # 탐색한 문자열 스택에 저장
                temp_length += 1    # 미중복 문자열 길이 1 증가
                
            if max_length < temp_length:
                max_length = temp_length

        return max_length