# 单调栈
def largestRectangleArea(heights: [int]) -> int:
    n = len(heights)
    left, right = [0] * n, [0] * n
    mono_stack = []
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)

    mono_stack = []
    for i in range(n - 1, -1, -1):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        right[i] = mono_stack[-1] if mono_stack else n
        mono_stack.append(i)

    result = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
    return result

if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    result = largestRectangleArea(heights)
    print(result)