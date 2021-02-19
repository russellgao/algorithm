def wordBreak(s: str, wordDict: [str]) -> bool:
    wordDictSet = {}
    maxlen = 0
    for item in wordDict:
        wordDictSet[item] = True
        if len(item) > maxlen:
            maxlen = len(item)
    length = len(s)
    dp = [False] * (length + 1)
    dp[0] = True
    for i in range(1, length + 1):
        for j in range(0, i):
            if dp[j] and wordDictSet.get(s[j:i]):
                dp[i] = True
                break
    return dp[length]

if __name__ == "__main__" :
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    result = wordBreak(s, wordDict)
    print(result)