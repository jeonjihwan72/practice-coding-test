class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 0:
            x *= -1
            x = str(x)
            x = x[::-1]
            x = int(x)
            x *= -1
            
            if x > 2**31 or x < -(2**31):
                return 0
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
            
            if x > 2**31 or x < -(2**31):
                return 0

        return x