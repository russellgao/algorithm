
def reverseString(str1) :
    """
    用递归的方法反转字符串
    :param list1: 字符串也数组的形式给出
    :return:
    """
    if not str1 :
        return None
    if len(str1) == 1 :
        return str1[0]
    return reverseString(str1[1:]) + str1[0]


if __name__ == "__main__" :
    str1 = "abcdefg"
    a = reverseString(str1)
    