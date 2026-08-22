class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = 0
        max_height = 0
        max_water = 0
        ptr_l, ptr_r = 0, len(heights) - 1

        while ptr_l < ptr_r:
            width = ptr_r - ptr_l
            max_height = min(heights[ptr_r], heights[ptr_l])
            current_water = max_height * width
            max_water = max(current_water, max_water)

            if heights[ptr_l] > heights[ptr_r]:
                ptr_r -=1

            else:
                ptr_l += 1 

        return max_water