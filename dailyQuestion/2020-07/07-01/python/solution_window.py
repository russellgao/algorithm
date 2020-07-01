def findLength(A: [int], B: [int]) -> int:
    def maxLength(addA: int, addB: int, length: int) -> int:
        ret = k = 0
        for i in range(length):
            if A[addA + i] == B[addB + i]:
                k += 1
                ret = max(ret, k)
            else:
                k = 0
        return ret

    n, m = len(A), len(B)
    ret = 0
    for i in range(n):
        length = min(m, n - i)
        ret = max(ret, maxLength(i, 0, length))
    for i in range(m):
        length = min(n, m - i)
        ret = max(ret, maxLength(0, i, length))
    return ret

if __name__ == "__main__" :

    A = [1,2,3,2,1]
    B = [3,2,1,4,7]

    a = A[0:1] == B[2:3]
    result = findLength(A,B)
    print(result)
