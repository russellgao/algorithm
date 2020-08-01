import heapq


def smallestRange(nums: [[int]]) -> [int]:
    rangeLeft, rangeRight = -10 ** 9, 10 ** 9
    maxValue = max(vec[0] for vec in nums)
    priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
    heapq.heapify(priorityQueue)

    while True:
        minValue, row, idx = heapq.heappop(priorityQueue)
        if maxValue - minValue < rangeRight - rangeLeft:
            rangeLeft, rangeRight = minValue, maxValue
        if idx == len(nums[row]) - 1:
            break
        maxValue = max(maxValue, nums[row][idx + 1])
        heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

    return [rangeLeft, rangeRight]



if __name__ == "__main__" :
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    result = smallestRange(nums)
    print(result)