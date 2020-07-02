def kthSmallest(matrix: [[int]], k: int) -> int:
    n = len(matrix)

    def check(mid):
        i, j = n - 1, 0
        num = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1
        return num >= k

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) >> 1
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]

    result = kthSmallest(matrix, 8)
    print(result)
