def longestCommonPrefix(strs: [str]) -> str:
    if not strs:
        return ""

    length, count = len(strs[0]), len(strs)
    for i in range(length):
        c = strs[0][i]
        if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            return strs[0][:i]

    return strs[0]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
