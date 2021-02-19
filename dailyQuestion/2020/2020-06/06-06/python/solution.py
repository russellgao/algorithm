
def longestConsecutive(nums: [int]) -> int:
    nums = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            current_len = 1
            while current + 1 in nums:
                current += 1
                current_len += 1
            longest = max(longest, current_len)
    return longest

if __name__ == "__main__" :
    nums = [100, 4, 200, 1, 3, 2]
    result = longestConsecutive(nums)
    print(result)
