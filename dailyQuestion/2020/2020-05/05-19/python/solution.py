class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        count = 1
        flag = True
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                flag = self.validate(s[i:j]) or self.validate(s[i + 1:j + 1])
                break
        return flag

    def validate(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__" :
    s = "ebcbbececabbacecbbcbe"

    a = "abcdef"
    c = a[1:2]
    result = validPalindrome(s)
    print(result)