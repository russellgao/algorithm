def longestPalindrome(s: str) -> str :
    """
    最长子串
    动态规划解法
    :param s:
    :return:
    """
    n = len(s)
    result = ""
    dp = [[False] * n for _ in range(n)]
    for l in range(n) :
        for i in range(n-l) :
            j = i + l
            if l == 0 :
                dp[i][j] = True
            elif l == 1 :
                if s[i] == s[j] :
                    dp[i][j] = True
            else :
                if s[i] == s[j] :
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and l + 1 > len(result) :
                result = s[i:j+1]
    return result


def longestPalindrome2(s: str) -> str :
    """
    最长子串
    中心扩展法
    :param s:
    :return:
    """
    if not s :
        return ""
    start,end = 0,0
    for i in range(len(s)) :
        left1, right1 = expandAroundCenter(s,i,i)
        left2, right2 = expandAroundCenter(s,i,i+1)
        if right1 - left1 > end - start :
            start, end = left1, right1
        if right2 - left2 > end - start :
            start, end = left2, right2
    return s[start:end+1]

def expandAroundCenter(s: str, left: int, right: int) -> (int,int) :
    """
    寻找最长子串
    :param s:
    :param left:
    :param right:
    :return:
    """
    while left >= 0 and right < len(s) and s[left] == s[right] :
        left -= 1
        right += 1
    return left+1,right-1


if __name__ == "__main__" :
    a = "babad"
    result = longestPalindrome(a)
    print(result)


