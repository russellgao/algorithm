def countBinarySubstrings(s: str) -> int:
    if not s :
        return 0
    pre,cur = 0 , 0
    count = 1
    result = 0
    for i in range(1,len(s)) :
        if s[i] != s[i-1] :
            pre,cur = cur,count
            result += min(pre,cur)
            count =1
            continue
        count += 1
    result += min(cur,count)
    return result


if __name__ == "__main__" :
    s = "00110011"
    result = countBinarySubstrings(s)
    print(result)