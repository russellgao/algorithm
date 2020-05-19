# 位运算的常用操作

def bit_or(a: int, b: int) -> int:
    """
    | 或 运算
    :param a:
    :param b:
    :return:
    """
    return a | b


def bit_and(a: int, b: int) -> int:
    """
    & 与运算
    :param a:
    :param b:
    :return:
    """
    return a & b


def bit_yihuo_(a: int, b: int) -> int:
    """
    ^ 异或运算
    :param a:
    :param b:
    :return:
    """
    return a ^ b


def bit_not(a: int) -> int:
    """
    ~ 取反
    :param a:
    :return:
    """
    return ~a


def count_1(a: int) -> int:
    """
    计算数值的二进制表示的1的数量
    :param a:
    :return:
    """
    count = 0
    while (a):
        a = a & a - 1
        count += 1
    return count


def abs(a: int) -> int:
    """
    求绝对值
    :param a:
    :return:
    """
    i = a >> 31
    result = (a ^ i) - i
    return result


def reversal(a: int) -> int:
    """
    求相反数
    :param a:
    :return:
    """
    return ~a + 1


def swap(a: int, b: int) -> (int, int):
    """
    交换两个数
    :param a:
    :param b:
    :return:
    """
    a ^= b  # a = (a^b)
    b ^= a  # b = b ^ a = b ^ a ^ b
    a ^= b  # a = a ^ b = a ^ a ^ b
    return a, b

def add(a: int, b: int) -> int:
    """
    两数求和
    :param a:
    :param b:
    :return:
    """
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    while b != 0:
        carry = a & b
        a ^= b
        b = ((carry) << 1) & 0xFFFFFFFF
    return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)

if __name__ == "__main__":
    a = 0xFFFFFFFF
    b = 9
    c = bit_and(a, b)
