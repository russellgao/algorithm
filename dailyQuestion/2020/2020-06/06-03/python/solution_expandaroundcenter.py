def countSubstrings(s: str) -> int:
    def expendAroundCentor(s, i, j):
        result = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            result += 1
            i -= 1
            j += 1

        return result

    result = 0
    if not s:
        return result
    for i in range(len(s)):
        result += expendAroundCentor(s, i, i)
        result += expendAroundCentor(s, i, i + 1)

    return result


if __name__ == "__main__":
    s = "aaa"
    result = countSubstrings(s)
    print(result)
