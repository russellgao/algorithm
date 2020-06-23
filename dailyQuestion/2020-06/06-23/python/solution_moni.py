def addBinary(a: str, b: str) -> str:
    n_a = len(a)
    n_b = len(b)
    max_n = max(n_a, n_b)
    a = a.rjust(max_n, "0")
    b = b.rjust(max_n, "0")
    jin_bit = 0
    result = ""
    for i in range(max_n - 1, -1, -1):
        tmp_a = int(a[i])
        tmp_b = int(b[i])
        tmp = tmp_a + tmp_b + jin_bit
        result = "{}{}".format(tmp % 2, result)
        jin_bit = tmp // 2
    if jin_bit != 0:
        result = "{}{}".format(1, result)
    return result

if __name__ == "__main__" :
    a = "11"
    b = "11"
    c = "11".rjust(2,"0")
    result = addBinary(a,b)
    print(result)