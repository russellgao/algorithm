# 暴力题解法
def largestRectangleArea(heights: [int]) -> int:
    """
    柱状图中最大的矩形
    :param heights:
    :return:
    """
    result = 0
    for i in range(len(heights)):
        height = heights[i]
        left, right = i, i
        while left - 1 >= 0 and heights[left - 1] >= height:
            left -= 1
        while right + 1 < len(heights) and heights[right + 1] >= height:
            right += 1
        result = max(result, (right - left + 1) * height)

    return result


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    result = largestRectangleArea(heights)
    print(result)
