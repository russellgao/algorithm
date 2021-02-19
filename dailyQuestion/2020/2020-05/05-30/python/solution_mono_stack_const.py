# 单调栈 + 常数优化
def largestRectangleArea(heights: [int]) -> int:
    n = len(heights)
    left = [0] * n
    right = [n] * n
    mono_stack = []
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            right[mono_stack[-1]] = i
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)
    result = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if heights else 0
    return result


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    result = largestRectangleArea(heights)
    print(result)
