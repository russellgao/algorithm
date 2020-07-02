def kthSmallest(matrix: [[int]], k: int) -> int:
    p = sorted(sum(matrix, []))
    return p[k - 1]


if __name__ == "__main__":
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    result = kthSmallest(matrix, 8)
    print(result)
