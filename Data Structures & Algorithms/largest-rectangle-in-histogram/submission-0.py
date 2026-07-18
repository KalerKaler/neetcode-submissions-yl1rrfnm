class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0
        popCount = 0

        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(height * (i - index), maxArea)
                start = index
            
            stack.append([start, heights[i]])
        
        i += 1
        while stack:
            maxArea = max(stack[-1][1] * (i - stack[-1][0]), maxArea)
            stack.pop()

        return maxArea