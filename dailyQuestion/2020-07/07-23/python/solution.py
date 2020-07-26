def isUgly(num: int) -> bool:
    if num < 1 :
        return False
    if num < 7 :
        return True
    if num % 2 == 0 :
        num /= 2
    elif num % 3 == 0 :
        num /= 3
    elif num % 5 == 0 :
        num /= 5
    else :
        return False
    return isUgly(num)

if __name__ == "__main__" :
    num = 34
    s = isUgly(num)
    print(s)