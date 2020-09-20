def countNumbersWithUniqueDigits(n: int) -> int:
    if n == 0 :
        return 1
    first, second = 10, 9
    for i in range(1,n) :
        second *= 10-i
        first += second
    return first

if __name__ == "__main__" :
    result = countNumbersWithUniqueDigits(3)
    print(result)
