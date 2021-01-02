class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]  # stack will contain indexes
        heights.append(0)  # dummy value for popping all elements from stack
        ans = 0
        for i in range(len(heights)):
            height = heights[i]
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans
