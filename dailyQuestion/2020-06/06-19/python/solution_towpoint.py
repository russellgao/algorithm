def isPalindrome(s: str) -> bool:
    if not s:
        return True
    i, j = 0, len(s) - 1
    while i <= j:
        if not ((s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0") and s[i] <= "9"):
            i += 1
            continue
        if not ((s[j] >= "a" and s[j] <= "z") or (s[j] >= "A" and s[j] <= "Z") or (s[j] >= "0") and s[j] <= "9"):
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    result = isPalindrome(s)
    print(result)
