class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        maxVolume = 0 
        for r in range(1, len(height)): 
            minHeight = min(height[l], height[r])
            maxVolume = max(maxVolume, (r-l)*minHeight)
            if (height[l] < height[r]): 
                l = r
                maxVolume = max(maxVolume, (r-l)*minHeight)
        return maxVolume