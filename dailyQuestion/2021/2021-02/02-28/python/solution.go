class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isAdd = True
        isReduce = True
        for i in range(len(A) - 1) :
            if A[i] > A[i+1] :
                isAdd = False
            if A[i] < A[i+1] :
                isReduce = False
        return isAdd or isReduce