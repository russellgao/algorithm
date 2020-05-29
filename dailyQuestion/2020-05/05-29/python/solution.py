# 写法一
def rob(nums: [int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n < 3:
        return max(nums)
    for i in range(2, n):
        nums[i] += max(nums[:i - 1])
    return max(nums)


def rob2(nums: [int]) -> int:
    if not nums:
        return 0

    size = len(nums)
    if size == 1:
        return nums[0]

    dp = [0] * size
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, size):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[size - 1]


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 7]
    s1 = rob2(nums)
    s2 = rob(nums)

    print(s1 == s2)
