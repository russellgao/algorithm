import math

# 方法一 珍珠计算器法
def mySqrt1(x:int) -> int :
    """

    :param x:
    :return:
    """
    if x == 0 :
        return 0
    result = int(math.exp(0.5 * math.log(x)))
    return result + 1 if (result + 1) ** 2 else result

# 二分法
def mySqrt2(x:int) -> int :
    """

    :param x:
    :return:
    """
    if x == 0 :
        return 0
    left,right,result = 0,x,-1
    while left <= right :
        mid = (left + right) >> 1
        if mid ** 2 <= x :
            result = mid
            left = mid + 1
        else :
            right = mid - 1
    return result

# 牛顿迭代法
def mySqrt3(x:int) -> int :
    """

    :param x:
    :return:
    """
    if x == 0:
        return 0
    c, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + c / x0)
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi
    return int(x0)

if __name__ == "__main__" :
    x = 5
    a = mySqrt2(x)
    print(a)