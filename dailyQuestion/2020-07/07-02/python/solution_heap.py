import heapq
def kthSmallest(matrix: [[int]], k: int) -> int:
    n = len(matrix)
    p = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(p)
    for i in range(k - 1):
        num, i, j = heapq.heappop(p)
        if j < n - 1:
            heapq.heappush(p, (matrix[i][j + 1], i, j + 1))
    return heapq.heappop(p)[0]


if __name__ == "__main__":
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]

    result = kthSmallest(matrix, 8)
    print(result)
