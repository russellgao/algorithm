def subSort(array: [int]) -> [int]:
    n = len(array)
    first,last = -1,-1
    if n == 0 :
        return [first,last]
    min_a = float("inf")
    max_a = float("-inf")
    for i in range(n) :
        if array[i] >= max_a :
            max_a = array[i]
        else :
            last = i
        if array[n-1-i] <= min_a :
            min_a = array[n-1-i]
        else :
            first = n-i-1
    return [first,last]

if __name__ == "__main__" :
    array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    result = subSort(array)
    print(result)