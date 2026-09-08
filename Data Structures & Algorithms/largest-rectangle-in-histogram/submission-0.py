class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        # O(n) + O(n)
        for i in range(len(heights)):                   # O(n)
            while stack and heights[stack[-1]] > heights[i]:     # O(n) for both while loops
                element = stack.pop()
                nge = i
                pge = stack[-1] if stack else -1
                res = max(res, heights[element] * (nge - pge - 1))
            stack.append(i)

        while stack:
            element = stack.pop()
            nge = len(heights)
            pge = stack[-1] if stack else -1
            res = max(res, heights[element] * (nge - pge - 1))

        return res