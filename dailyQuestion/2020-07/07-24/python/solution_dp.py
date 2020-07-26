class Ugly:
    def __init__(self) :
        self.nums = [1]
        i2 = i3 = i5 = 0
        for i in range(1690) :
            ugly = min(self.nums[i2] * 2, self.nums[i3] * 3, self.nums[i5] * 5)
            self.nums.append(ugly)
            if ugly == self.nums[i2] * 2 :
                i2 += 1
            if ugly == self.nums[i3] * 3 :
                i3 += 1
            if ugly == self.nums[i5] * 5 :
                i5 += 1

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]

if __name__ == "__main__" :
    s = Solution()
    result = s.nthUglyNumber(10)
    print(result)
