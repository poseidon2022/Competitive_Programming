class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                net_height = min(height[i], height[stack[-1]]) - height[top]
                ans += net_height * width
                
            stack.append(i)
        
        return ans