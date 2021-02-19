def longestCommonPrefix(strs: [str]) -> str:
    n = len(strs)
    result = ""
    if not n:
        return result
    result = strs[0]
    for i in range(1, n):
        result = result[:len(strs[i])]
        result_len = len(result)
        for j in range(min(len(strs[i]), result_len)):
            if result[j] != strs[i][j]:
                result = result[:j]
                break
    return result


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
