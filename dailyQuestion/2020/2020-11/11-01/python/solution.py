from functools import lru_cache

def wordBreak(s: str, wordDict: [str]) -> [str]:
    wordmap = {}
    for item in wordDict :
        wordmap[item] = True
    n = len(s)
    dp = [[]] * n
    result = []

    # 通过缓存避免超时
    @lru_cache(None)
    def backtrace(index) :
        if dp[index] :
            return dp[index]
        wordList = []
        for i in range(index+1,n) :
            word = s[index:i]
            if wordmap.get(word) :
                for nexttrace in backtrace(i) :
                    tmp = [word]
                    tmp.extend(nexttrace)
                    wordList.append(tmp)
        word = s[index:]
        if wordmap.get(word) :
            wordList.append([word])
        dp[index] = wordList
        return wordList
    for item in backtrace(0) :
        result.append(" ".join(item))
    return result


if __name__ == "__main__" :
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    result = wordBreak(s,wordDict)
    print(result)
