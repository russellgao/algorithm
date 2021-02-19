
def countSubstrings(s: str) -> int:
    result = 0
    if not s :
        return result
    len_s = len(s)
    dp = [[False]* len_s for _ in range(len_s)]
    for length in range(len_s) :
        for i in range(len_s - length) :
            j = i + length
            if length == 0 :
                dp[i][j] = True
            elif length == 1 :
                if s[i] == s[j] :
                    dp[i][j] = True
            else :
                if s[i] == s[j] :
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] :
                result += 1
    return result

if __name__ == "__main__" :
    s = "aaa"
    result = countSubstrings(s)
    print(result)

