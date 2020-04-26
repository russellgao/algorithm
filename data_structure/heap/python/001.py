import heapq

arr = [5, 8, 6, 3, 4, 7, 0, 1, 2, 9]
heap = []

# heapq.heapify(list) 将 数据转化为堆 ,在list 的基础上直接堆化
heapq.heapify(arr)

# heapq.heappush(heap,item), 往堆中增加元素，增加完了之后还是一个堆
heapq.heappush(arr,5)

# heapq.heappop(heap) ,删除最小元素
a1 = heapq.heappop(arr)

# heapq.heapreplace(heap, item) ,删除最小元素，之后在添加新元素item
a2 = heapq.heapreplace(arr, 8)

# heapq.heappushpop(heap, item) 首先判断添加元素值与堆的第一个元素之对比，如果大则删除第一个元素，然后添加新的元素值，否则不更改
a3 = heapq.heappushpop(arr,5)

# heapq.merge(iterables) 将多个堆合并,必须是堆才行，否则得出可能不是最小堆
arr1 = [1,2,4]
arr2 = [4,3,1]
heapq.heapify(arr1)
heapq.heapify(arr2)
a4 = list(heapq.merge(arr, arr1, arr2))

# heapq.nlargest(n, heap) 查询堆中最大的n个元素
a5 = heapq.nlargest(3, arr)

# heapq.nsmallest(n, heap)
a6 = heapq.nsmallest(3,arr)

print()