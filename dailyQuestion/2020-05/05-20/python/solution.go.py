def findTheLongestSubstring(s: str) -> int:
    """
    每个元音包含偶数次的最长子字符串
    :param s:
    :return:
    """
    result = 0
    status = 0
    pos = [-1] * (1 << 5)
    pos[0] = 0
    for i in range(len(s)):
        tmp = s[i]
        if tmp == "a":
            status ^= 1 << 0
        elif tmp == "e":
            status ^= 1 << 1
        elif tmp == "o":
            status ^= 1 << 2
        elif tmp == "i":
            tmp ^= 1 << 3
        elif tmp == "u":
            tmp ^= 1 << 4
        if pos[status] >= 0:
            result = max(result, i + 1 - pos[status])
        else:
            pos[status] = i + 1
    return result


if __name__ == "__main__":
    s = "babbbbeabe"
    result = findTheLongestSubstring(s)
    print(result)
