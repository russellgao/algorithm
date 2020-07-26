import collections
import heapq

def topKFrequent(nums: [int], k: int) -> [int]:
    count = collections.Counter(nums)
    result = heapq.nlargest(k,count.keys(),key=count.get)
    return result

if __name__ == "__main__" :
    nums = [1,1,1,2,2,3]
    result = topKFrequent(nums,2)
    print(result)