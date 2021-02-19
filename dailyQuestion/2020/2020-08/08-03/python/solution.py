def addStrings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    tmp = 0
    result = ""
    while i >= 0 or j >= 0:
        if i >= 0:
            tmp += int(num1[i])
            i -= 1
        if j >= 0:
            tmp += int(num2[j])
            j -= 1
        result = str(tmp % 10) + result
        tmp //= 10
    if tmp != 0:
        result = str(tmp) + result
    return result


if __name__ == "__main__":
    num1 = "999999"
    num2 = "99"
    result = addStrings(num1, num2)
    print(result)
