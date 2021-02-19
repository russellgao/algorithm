
def lengthOfLongestSubstring(s: str) -> int:
    tmp = set()
    result = 0
    j = 0
    n = len(s)
    for i in range(n) :
        if i != 0 :
            tmp.remove(s[i-1])
        while j < n and s[j] not in tmp :
            tmp.add(s[j])
            j += 1
        result = max(result, j - i)
    return result

if __name__ == "__main__" :
    a = [23,4,5,6]

    s = "abcabcbb"
    result = lengthOfLongestSubstring(s)
    print(result)
