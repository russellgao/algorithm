class NumArray:

    def __init__(self, nums: [int]):
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == "__main__":
    nums = [2, 1, 7, 8, 5, 9]
    obj = NumArray(nums)
    print(obj.sumRange(0, 4))
    print(obj.sumRange(1, 4))
    print(obj.sumRange(2, 4))
    print(obj.sumRange(3, 4))
    print(obj.sumRange(4, 4))
