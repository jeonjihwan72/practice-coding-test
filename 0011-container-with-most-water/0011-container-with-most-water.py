class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # # 그리드 방식 접근
        # max_container = 0

        # for i in range(0, len(height)):
        #     for j in range(i+1, len(height)):
        #         width_water = j-i
        #         height_water = min(height[i], height[j])
        #         container = width_water * height_water
        #         if container > max_container:
        #             max_container = container

        # return max_container

        # 2개의 포인터를 활용한 방법
        right_pointer = len(height)-1
        left_pointer = 0

        max_container = 0

        while right_pointer > left_pointer:
            container_width = right_pointer - left_pointer
            
            if height[left_pointer] <= height[right_pointer]:
                less_height_pointer = left_pointer
            else: less_height_pointer = right_pointer

            container_height = height[less_height_pointer]
            container = container_width * container_height
            
            if container > max_container:
                max_container = container
            
            if less_height_pointer == right_pointer:
                right_pointer -= 1
            else:
                left_pointer += 1
        
        return max_container
