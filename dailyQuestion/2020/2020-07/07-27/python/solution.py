def isSubsequence(s: str, t: str) -> bool:
    """
    原始版
    :param s:
    :param t:
    :return:
    """
    if len(s) > len(t):
        return False
    if s == t:
        return True
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
            if i == len(s):
                return True
        else:
            j += 1
    return False

def isSubsequence_optimize(s: str, t: str) -> bool:
    """

    :param s:
    :param t:
    :return:
    """
    m ,n = len(s) , len(t)
    i = j = 0
    while i < m and j < n :
        if s[i] == t[j] :
            i += 1
        j += 1
    return i == m

if __name__ == "__main__" :
    s = "abc"
    t = "ahbgdc"
    result = isSubsequence(s,t)
    print(result)