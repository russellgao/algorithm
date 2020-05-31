from collections import deque

# deque 对象
# class collections.deque([iterable[, maxlen]])
# 返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，
# 从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
#
# Deque队列是由栈或者queue队列生成的（发音是 “deck”，”double-ended queue”的简称）。
# Deque 支持线程安全，内存高效添加(append)和弹出(pop)，
# 从两端都可以，两个方向的大概开销都是 O(1) 复杂度。
#
# 虽然 list 对象也支持类似操作，不过这里优化了定长操作和 pop(0) 和 insert(0, v) 的开销。
# 它们引起 O(n) 内存移动的操作，改变底层数据表达的大小和位置。
#
# 如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。
# 否则，deque就限定到指定最大长度。
# 一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。
# 限定长度deque提供类似Unix filter tail 的功能。它们同样可以用与追踪最近的交换和其他数据池活动。


queue1 = deque(range(3,10))

print(queue1[4]) # 7
queue1.append(111)
queue1.appendleft(222)
print(queue1) # deque([222, 3, 4, 5, 6, 7, 8, 9, 111])

print()