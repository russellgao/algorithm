class Solution:
    def flipAndInvertImage(self, A: [[int]]) -> [[int]]:
        for row in A :
            left, right = 0 , len(row) -1
            while left < right :
                if row[left] == row[right] :
                    row[left] ^= 1
                    row[right] ^= 1
                left += 1
                right -= 1
            if left == right :
                row[left] ^= 1
        return A

if __name__ == "__main__" :
    s = Solution()
    a1 = [[1,1,0],[1,0,1],[0,0,0]]
    a2 = s.flipAndInvertImage(a1)
    print(a2)
