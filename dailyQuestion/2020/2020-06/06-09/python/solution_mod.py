# 动态求余法
def translateNum(num: int) -> int:
    f_1 = f_2 = 1
    while num:
        pre = num % 100
        f = f_1 + f_2 if pre >= 10 and pre <= 25 else f_1
        f_2 = f_1
        f_1 = f
        num = num // 10
    return f_1

if __name__ == '__main__' :
    num = 12258
    result = translateNum(num)
    print(result)
