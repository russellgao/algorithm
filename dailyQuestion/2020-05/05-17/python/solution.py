def insertBits(N: int, M: int, i: int, j: int) -> int:
    return ((N >> (j + 1) << (j + 1)) | ((N >> i << i) ^ N)) | M << i

if __name__ == "__main__" :
    N = 1024
    M = 19
    j = 6
    i = 2
    result = insertBits(N,M,i,j)
    print(result)