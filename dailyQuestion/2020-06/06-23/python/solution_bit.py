def addBinary(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    while b:
        result = a ^ b
        carry = (a & b) << 1
        a = result
        b = carry
    return bin(a)[2:]

if __name__ == "__main__" :
    a = "11"
    b = "1"
    c = "11".rjust(2,"0")
    result = addBinary(a,b)
    print(result)