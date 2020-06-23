
# 转换为10进制，相加再转换为2进制
def addBinary(a: str, b: str) -> str:
    a = int(a,2)
    b = int(b,2)
    c = a + b
    return bin(c)[2:]

if __name__ == "__main__" :
    a = "11"
    b = "1"
    result = addBinary(a,b)
    print(result)
