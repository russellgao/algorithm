
# 用set来表示一个无序不重复元素的序列。set的只要作用就是用来给数据去重。
# 可以使用大括号 { } 或者 set() 函数创建集合，但是注意如果创建一个空集合必须用 set() 而不是 { }，因为{}是用来表示空字典类型的

# 创建
persion1 = {"a", "b", "c"}
persion2 = set(range(5))
persion3 = set(["b", "c", "d"])

# 更新,会把差异化的地方更新到persion1
persion1.update(persion3)

# 删除一个元素
persion1.remove("b")

# 增加一个元素
persion1.add("e")

# set 中随机删除一个元素
tmp1 = persion1.pop()

# 把set 清空
persion2.clear()

# copy 是一个深copy ,用等号复制一个变量则是浅copy
# 可以通过id 查看
tmp2 = persion1.copy()
tmp3 = persion1
print(id(persion1))
print(id(tmp2))
print(id(tmp3))
tmp2.add("f")
tmp3.add("f")

# 返回两个set 的合集，会有一个新的set 返回
tmp4 = persion1.union(persion3)

# 返回persion1 相对于 persion3 的差集，即persion1 中的元素不在 persion3 中
tmp5 = persion1.difference(persion3)

# # 和 difference类似，直接在persion1的基础上update,不会返回新的set
# persion1.difference_update(persion3)

# 返回persion1 和 persion3 的 叉集 ，即 persion1 和 persion3 中都存在的元素
tmp6 = persion1.intersection(persion3)

# # 和intersection 类似，直接在persion1的基础上update，不会返回新的set
# persion1.intersection_update(persion3)

# 丢弃一个元素
# 和remove 的一个区别是，remove 的元素必须存在于set中，否则会报错 ，discard 可以不是当中的元素
persion1.discard("d")

# 堆成的求差集，即返回 persion1相对于persion3的差集 于 persion3相对于persion1的差集的合集
tmp7 = persion1.symmetric_difference(persion3)

# # 和 symmetric_difference 类似，直接在persion1的基础上update，不会返回新的set
# persion1.symmetric_difference_update(persion3)

# 是否不相交的，即判断是否有两个set 中是否有相同的元素
tmp8 = persion1.isdisjoint(persion3)
tmp9 = persion1.isdisjoint(persion2)

# 是否是子集,即 persion3 是否是 persion1 的子集
tmp10 = persion1.issubset(persion3)
tmp11 = persion1.issubset(tmp3)

# 是否是父集，集 persion3 是否是 perions1 的子集，和 issubset 作用是相反的
tmp12 = persion1.issuperset(persion3)
tmp13 = persion1.issuperset(tmp3)


print()


