def maxScoreSightseeingPair(A: [int]) -> int:
    result = 0
    mx = A[0]
    for j in range(1, len(A)):
        if mx + A[j] - j > result:
            result = mx + A[j] - j
        if A[j] + j > mx:
            mx = A[j] + j
    return result

if __name__ == "__main__" :
    A = [8,1,5,2,6]
    result = maxScoreSightseeingPair(A)
    print(result)

