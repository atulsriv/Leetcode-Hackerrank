from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0 # amount of water

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            if cur_area > max_area:
                max_area = cur_area

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area