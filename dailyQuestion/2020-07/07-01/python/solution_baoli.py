def findLength(A: [int], B: [int]) -> int:
    len_A = len(A)
    len_B = len(B)
    min_len = min(len_A, len_B)
    result = 0
    for i in range(len_A) :
        for j in range(len_B) :
            k = 0
            while i + k < min_len and j+k < min_len and A[i+k] == B[j+k] :
                k += 1
            result = max(result, k )
    return result

if __name__ == "__main__" :


    A = [1,2,3,2,1]
    B = [3,2,1,4,7]

    a = A[0:1] == B[2:3]
    result = findLength(A,B)
    print(result)
