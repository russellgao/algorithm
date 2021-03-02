class NumMatrix:

    def __init__(self, matrix: [[int]]):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + matrix[i][j]
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][
            col1]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    obj = NumMatrix(matrix)
    res= obj.sumRegion(1,1,3,3)
    print(res)
