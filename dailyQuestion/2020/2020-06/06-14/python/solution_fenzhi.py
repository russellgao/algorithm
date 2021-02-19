def longestCommonPrefix(strs: [str]) -> str:
    def lcp(start, end):
        if start == end:
            return strs[start]
        mid = (start + end) >> 1
        leftLcp = lcp(start, mid)
        rightLcp = lcp(mid + 1, end)
        minLcp = min(len(leftLcp), len(rightLcp))
        for i in range(minLcp):
            if leftLcp[i] != rightLcp[i]:
                return leftLcp[:i]
        return leftLcp[:minLcp]

    return lcp(0, len(strs) - 1) if strs else ""


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
