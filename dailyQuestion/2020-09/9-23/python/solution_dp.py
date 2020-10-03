def minimumOperations(leaves: str) -> int:
    def boolToInt(b) :
        if b :
            return 1
        return 0

    n = len(leaves)
    f = [ [float('inf')] * 3  for i in range(n)]
    f[0][0] = boolToInt(leaves[0]=='y')
    for i in range(1,n) :
        f[i][0] = f[i-1][0] + boolToInt(leaves[i]=='y')
        f[i][1] = min(f[i-1][0], f[i-1][1]) + boolToInt(leaves[i]=='r')
        if i >= 2 :
            f[i][2] = min(f[i-1][1], f[i-1][2]) + boolToInt(leaves[i] == 'y')
    return f[n-1][2]


if __name__ == "__main__" :
    result = minimumOperations("rrryyyrryyyrr")
    print(result)

