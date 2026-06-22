class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ###########################################
        #                예외 사항                     
        # 1. numRows = 1인 경우                    
        # 2. numRows보다 문자열의 길이가 짧은 경우
        ###########################################
        if numRows == 1 or numRows >= len(s):
            return s

        result_rows = [[] for _ in range(numRows)]

        direction = 1   # 방향성 결정 변수
        current_row = 0 # 현재 저장하고 있는 행의 위치

        for character in s:
            # 해당되는 행에 문자 저장
            result_rows[current_row].append(character)

            # 최상단 지점에 도달하면 방향을 아래로 전환
            if current_row == 0:
                direction = 1
            
            # 최하단 지점에 도달하면 방향을 위로 전환
            if current_row == numRows-1:
                direction = -1
            
            # 행 변환
            current_row += direction
        
        # 행들에 저장된 문자들을 문자열 형태로 이어 붙이기
        result = ""
        result = result.join(["".join(row) for row in result_rows])

        return result

