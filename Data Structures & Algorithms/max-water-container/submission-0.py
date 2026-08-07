class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        while (l < r):
            minHeight = min(heights[l],heights[r])
            water = (r - l) * minHeight
            maximum = max(maximum, water)
            if (minHeight == heights[l]):
                l += 1
            elif (minHeight == heights[r]):
                r -= 1
            else:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        return maximum