class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # max_palindrome = ""
        # palindrome_length = 0

        # for start in range(0, len(s)):
        #     for end in range(start, len(s)):
        #         check_target = s[start:end+1]
        #         if check_target == check_target[::-1] and len(check_target) >= palindrome_length:
        #             max_palindrome = check_target
        #             palindrome_length = len(check_target)

        # return max_palindrome                    

        if len(s) < 2 or s == s[::-1]:
            return s
            
        def expand(left, right):
            # 좌우 포인터가 범위 내에 있고, 두 글자가 같으면 계속 확장
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # while문을 빠져나올 때는 조건이 깨진 상태이므로 한 칸씩 안으로 좁혀서 반환
            return s[left + 1:right]

        result = ""
        for i in range(len(s)):
            # 1. 홀수 길이 팰린드롬 체크 (중심이 글자 하나인 경우 ex: "aba")
            p1 = expand(i, i)
            # 2. 짝수 길이 팰린드롬 체크 (중심이 글자 두 개인 경우 ex: "abba")
            p2 = expand(i, i + 1)
            
            # 기존 가장 긴 팰린드롬과 비교하여 갱신
            result = max(result, p1, p2, key=len)
            
        return result