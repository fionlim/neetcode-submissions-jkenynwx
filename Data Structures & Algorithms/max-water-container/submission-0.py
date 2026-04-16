class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            area = min_height * (right - left)
            print("area:", area)
            print("left:", left)
            print("right:", right)
            if area > max_area:
                max_area = area
            if heights[left] == min_height:
                left += 1
            else:
                right -= 1
        return max_area

         