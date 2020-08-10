def palindromePairs(words: [str]) -> [[int]]:
    indices = {}
    result = []
    n = len(words)

    def reverse(word):
        _w = list(word)
        n = len(word)
        for i in range(n >> 1):
            _w[i], _w[n - 1 - i] = _w[n - i - 1], _w[i]
        return "".join(_w)

    def isPalindromes(word: str, left: int, right:int) -> bool:
        for i in range(right - left + 1):
            if word[left + i] != word[right - i]:
                return False
        return True

    def findWord(word, left, right):
        v = indices.get(word[left:right+1])
        if v is not None :
            return v
        return -1

    for i in range(n):
        indices[reverse(words[i])] = i

    for i in range(n):
        word = words[i]
        m = len(word)
        for j in range(m + 1):
            if isPalindromes(word, j, m - 1) :
                leftid = findWord(word, 0 , j-1)
                if leftid != -1 and leftid != i :
                    result.append([i,leftid])
            if j > 0 and isPalindromes(word, 0,j-1) :
                leftid = findWord(word,j,m-1)
                if leftid != -1 and leftid != i :
                    result.append([i,leftid])
    return result

if __name__ == "__main__" :
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = palindromePairs(words)
    print(result)

