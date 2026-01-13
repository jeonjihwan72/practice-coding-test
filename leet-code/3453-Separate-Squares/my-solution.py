class Solution(object):
    
    std_line = 0.0
    initial = True
    bottom_line, top_line = 0.0, 0.0
    total_area, goal_area = 0.0, 0.0
    iteration = 0

    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        if (self.initial):
            bottom_borders = []
            top_borders = []
            for box in squares:
                bottom_borders.append(float(box[1]))
                top_borders.append(float(box[1])+float(box[2]))

            self.bottom_line = min(bottom_borders)
            self.top_line = max(top_borders)
            self.std_line = (self.top_line + self.bottom_line) / 2

            # todo: calculate total_area
            for box in squares:
                self.total_area += float(box[2]) ** 2

            self.goal_area = self.total_area / 2

            self.initial = False

        under_area = 0.0

        for box in squares:
            if (float(box[1]) >= self.std_line):
                pass
            elif ((float(box[1])+float(box[2])) <= self.std_line):
                under_area += float(box[2]) ** 2
            else:
                temp_area_x = float(box[2])
                temp_area_y = self.std_line - float(box[1])
                temp_area = temp_area_x * temp_area_y

                under_area += temp_area
        
        self.iteration += 1
        if (self.iteration == 100):
            return self.std_line

        if (under_area >= self.goal_area):
            self.top_line = self.std_line
            self.std_line = (self.bottom_line + self.std_line) / 2
            return self.separateSquares(squares)
        elif (under_area < self.goal_area):
            self.bottom_line = self.std_line
            self.std_line = (self.top_line + self.std_line) / 2
            return self.separateSquares(squares)        

        return self.std_line