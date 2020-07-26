import heapq
class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k :
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k :
            heapq.heappop(self.nums)
        return self.nums[0]

if __name__ == "__main__" :
    k = 3
    nums = [4,5,8,2]
    obj = KthLargest(k, nums)
    param_1 = obj.add(10)
    print(param_1)