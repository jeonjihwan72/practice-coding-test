class Solution(object):
    
    # def merge_array(nums1, nums2):
    #     # 시간 복잡도 O(log(m+n))은 두 배열의 이진 탐색의 시간복잡도와 동일하다
    #     merged_array = []   # 병합된 배열을 저장할 리스트
    #     nums1_point = 0 # nums1 에서 움직일 포인터
    #     nums2_point = 0 # nums2 에서 움직일 포인터

    #     while True:
    #         # 상호 비교 후 작은 쪽을 merged_array에 넣고 해당 포인터 1 이동
    #         if nums1[nums1_point] > nums2[nums2_point]:
    #             merged_array.append(nums2[nums2_point])
    #             nums2_point += 1
    #         else:
    #             merged_array.append(nums1[nums1_point])
    #             nums1_point += 1
            
    #         # 둘 중 하나가 모두 포함된 경우 다른 하나의 나머지를 모두 merged_array에 저장
    #         if nums1_point == len(nums1):
    #             merged_array += nums2[nums2_point:]
    #             break
    #         if nums2_point == len(nums2):
    #             merged_array += nums1[nums1_point:]
    #             break
        
    #     return merged_array
                                    
    
    
    def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     merged_array = merge_array(nums1, nums2)

    #     median_index = 0

    #     if len(merged_array) % 2 == 0:
    #         temp_mid_index = len(merged_array) // 2
    #         median = (merged_array[temp_mid_index] + merged_array[temp_mid_index-1]) / 2
    #     else:
    #         temp_mid_index = len(merged_array) // 2
    #         median = merged_array[temp_mid_index]
        
    #     return median
    
    # 항상 크기가 더 작은 배열을 기준으로 이진 탐색을 해야 O(log(min(m, n)))이 보장됩니다.
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            # A 배열의 중간 지점
            i = (l + r) // 2  
            # B 배열에서 A 배열이 가져간 만큼을 제외한 나머지 중간 지점
            j = half - i - 2  
            
            # 인덱스가 범위를 벗어날 때를 대비한 예외 처리 (음의 무한대, 양의 무한대)
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # 올바른 분할 지점을 찾은 경우 (A의 왼쪽이 B의 오른쪽보다 작고, B의 왼쪽이 A의 오른쪽보다 작을 때)
            if Aleft <= Bright and Bleft <= Aright:
                # 전체 개수가 홀수일 때
                if total % 2:
                    return min(Aright, Bright)
                # 전체 개수가 짝수일 때
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                
            elif Aleft > Bright:
                r = i - 1  # A의 탐색 범위를 왼쪽으로 줄임 (절반 탈락)
            else:
                l = i + 1  # A의 탐색 범위를 오른쪽으로 늘림 (절반 탈락)