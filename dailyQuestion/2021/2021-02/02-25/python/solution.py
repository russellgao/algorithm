
class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m) :
            for j in range(n) :
                res[j][i] = matrix[i][j]
        return res


if __name__ == "__main__" :
    s = Solution()
    matrix = [[1, 2, 3,6], [4, 5, 6,8], [7, 8, 9,4]]
    res = s.transpose(matrix)
    print(res)