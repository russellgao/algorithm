
def lengthOfLongestSubstring(s: str) -> int:
    tmp = set()
    n = len(s)
    j, result = 0, 0
    for i in range(n):
        if i != 0:
            # 左指针右移
            tmp.remove(s[i - 1])
        while j < n and s[j] not in tmp:
            tmp.add(s[j])
            # 右指针移动
            j += 1
        result = max(result, j - i)
    return result

if __name__ == "__main__" :
    a = [23,4,5,6]

    s = "abcabcbb"
    result = lengthOfLongestSubstring(s)
    print(result)
