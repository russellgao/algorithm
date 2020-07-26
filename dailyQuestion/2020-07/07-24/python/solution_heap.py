import heapq

class Ugly:
    def __init__(self) :
        # seen 用于记录有没有遍历过，也可以用heap 代替，但是效率低很多
        seen = {1,}
        self.nums = []
        heap = [1]
        for _ in range(1690) :
            current_num = heapq.heappop(heap)
            self.nums.append(current_num)
            for i in [2,3,5] :
                heap_num = current_num * i
                if heap_num not in seen :
                    seen.add(heap_num)
                    heapq.heappush(heap,heap_num)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u = Ugly()
        return u.nums[n-1]

if __name__ == "__main__" :
    s = Solution()
    result = s.nthUglyNumber(10)
    print(result)


