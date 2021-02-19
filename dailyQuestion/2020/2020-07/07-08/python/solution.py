def divingBoard(shorter: int, longer: int, k: int) -> [int]:
    result = []
    if k == 0 :
        return result
    if longer == shorter :
        result.append(shorter*k)
        return result
    for i in range(k,-1,-1) :
        item = shorter * i + (k-i) *longer
        result.append(item)
    return result

if __name__ == "__main__" :
    shorter = 1
    longer = 2
    k = 3
    result = divingBoard(shorter,longer,k)
    print(result)
