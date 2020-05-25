
def subtractProductAndSum(n: int) -> int:
    add = 0
    mul = 1
    while n :
        n, mod = divmod(n,10)
        add += mod
        mul *= mod
    return mul - add

if __name__ == "__main__" :
    n = 234
    result = subtractProductAndSum(n)
    print(result)

