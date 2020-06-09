
# 从左向右遍历
def translateNum(num: int) -> int:
    s = str(num)
    f_1 = f_2 = 1
    for i in range(2, len(s) + 1):
        pre = s[i - 2:i]
        f = f_1 + f_2 if pre >= "10" and pre <= "25" else f_1
        f_2 = f_1
        f_1 = f
    return f_1

# 从右向左遍历
def translateNum_2(num: int) -> int:
    s = str(num)
    f_1 = f_2 = 1
    for i in range(2, len(s) + 1):
        pre = s[i - 2:i]
        f = f_1 + f_2 if pre >= "10" and pre <= "25" else f_1
        f_2 = f_1
        f_1 = f
    return f_1

if __name__ == '__main__' :
    num = 12258
    result = translateNum(num)
    print(result)
