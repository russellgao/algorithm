import heapq

def getLeastNumbers(arr: [int], k: int) -> [int]:
    result = [-arr[i] for i in range(k)]
    heapq.heapify(result)
    for i in range(k, len(arr)):
        heapq.heappushpop(result, -arr[i])
    result = [-result[i] for i in range(k)]
    return result

if __name__ == "__main__" :
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    result = getLeastNumbers(arr,k)
    print(result)