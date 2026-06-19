class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 정석적인 방법 (시간 복잡도: O(n^2))
        
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i]+nums[j]==target):
        #             return [i,j]
        
        # return None
        
        # 정렬 후 좌우 양 끝에서 접근하여 찾는 방법
        # 시간 복잡도: O(n)

        left_index, right_index = 0, len(nums)-1    # 좌우 인덱스 초기 번호 설정

        sorted_list = sorted(enumerate(nums), key=lambda x:x[1])    # 인덱스 번호를 포함하여 오름차순 정렬
        result = [] # 결과를 담을 인덱스

        while(True):
            
            if left_index >= right_index:
                return None

            two_sum = sorted_list[left_index][1] + sorted_list[right_index][1]  # 좌우 간의 합산 결과 저장

            if two_sum > target:
                # 합산이 목표보다 크다는 것은 더해야 하는 수보다 큰 수를 더한 것이므로 우측 인덱스 1 빼기
                right_index -= 1
            elif two_sum < target:
                # 합산이 목표보다 작다는 것은 더해야 하는 수보다 작은 값을 더한 것이므로 좌측 인덱스 1 더하기
                left_index += 1
            else:
                # 합산이 목표와 같으므로 리스트 저장 후 반복문 탈출
                # sorted_list는 정렬된 복사본이므로 enumerate를 사용한 원본의 인덱스를 저장
                result = [sorted_list[left_index][0], sorted_list[right_index][0]]
                break
        
        return result
    