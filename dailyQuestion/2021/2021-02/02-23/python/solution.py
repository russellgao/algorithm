# !/usr/bin/env python

class Solution:
    def maxSatisfied(self, customers: [int], grumpy: [int], X: int) -> int:
        res = 0
        n = len(customers)
        for i in range(n) :
            if grumpy[i] == 0 :
                res += customers[i]
        _sum = 0
        for i in range(X) :
            if grumpy[i] == 1 :
                _sum += customers[i]
        tmp_sum = _sum
        for i in range(X, n) :
            if grumpy[i] == 1 :
                tmp_sum += customers[i]
            if grumpy[i-X] == 1 :
                tmp_sum -= customers[i-X]
            _sum = max(tmp_sum, _sum)
        return res + _sum



if __name__ == "__main__" :
    s = Solution()
    # customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # X = 3

    customers = [3, 2, 5]
    grumpy = [0, 1, 1]
    X = 2

    res = s.maxSatisfied(customers, grumpy, X)
    print(res)
