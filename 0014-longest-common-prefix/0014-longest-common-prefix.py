class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # result = ""
        # checker = True
        # temp = sorted(strs, key=lambda x: len(x))

        # for i in range(0, len(temp[0])):
        #     t = temp[0][i]
        #     for w in strs:
        #         if w[i] != t:
        #             checker = False
        #             break
            
        #     if checker == False:
        #         break
            
        #     result += t
        
        # return result

        result = ""
        # 사전식 오름차순으로 정렬되므로 처음과 끝이 서로 어두가 동일하다면 그 사이의 단어들도 같음을 보장한다.
        strs.sort()
        
        first = strs[0]
        last = strs[-1]

        for i in range(0, min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result += first[i]
        
        return result