def longestCommonPrefix(strs: [str]) -> str:
    def isCommonPrefix(length):
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count))

    if not strs:
        return ""

    minLength = min(len(s) for s in strs)
    low, high = 0, minLength
    while low < high:
        mid = (high - low + 1) // 2 + low
        if isCommonPrefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]



if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
