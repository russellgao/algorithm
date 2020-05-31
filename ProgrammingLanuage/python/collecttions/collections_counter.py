from collections import Counter

# Counter 对象
# 一个计数器工具提供快速和方便的计数
# 一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
# 它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。
# 计数可以是任何整数值，包括0和负数。 Counter 类有点像其他语言中的 bags或multisets。


color = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt1 = Counter(color) # 参数是一个可迭代对象，返回一个字典
print(cnt1) # Counter({'blue': 3, 'red': 2, 'green': 1})
print(cnt1["red"]) # 2
print(cnt1["klo"]) # 不存在默认为0， 不会抛出异常

cnt2 = Counter("gallahad")
print(cnt2)  # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})

cnt3 = Counter({'red': 4, 'blue': 2})
print(cnt3) # Counter({'red': 4, 'blue': 2})

cnt4 = Counter(cats=8,dogs = 9)
print(cnt4)  # Counter({'dogs': 9, 'cats': 8})

# 计数器对象除了字典方法以外，还提供了三个其他的方法：elements()
# elements()
# 返回一个迭代器，其中每个元素将重复出现计数值所指定次。
# 元素会按首次出现的顺序返回。 如果一个元素的计数值小于一，elements() 将会忽略它。

cnt5 = Counter(a=4, b=2, c=0, d=-2)
print(list(cnt5.elements())) # ['a', 'a', 'a', 'a', 'b', 'b']

# most_common(n)
# 返回一个列表，其中包含 n 个最常见的元素及出现次数，按常见程度由高到低排序。
# 如果 n 被省略或为 None，most_common() 将返回计数器中的 所有 元素。
# 计数值相等的元素按首次出现的顺序排序：
print(cnt1.most_common(2)) # [('blue', 3), ('red', 2)]

# subtract([iterable-or-mapping])
# 从 迭代对象 或 映射对象 减去元素。
# 像 dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。

cnt6 = Counter(a=4, b=2, c=0, d=-2)
cnt6.subtract({"a":1,"d":-8})
print(cnt6)

# fromkeys
# 这个类方法没有在 Counter 中实现。

# update([iterable-or-mapping])
# 从 迭代对象 计数元素或者 从另一个 映射对象 (或计数器) 添加。
# 像 dict.update() 但是是加上，而不是替换。另外，迭代对象 应该是序列元素，而不是一个 (key, value) 对。

print()