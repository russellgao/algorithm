from collections import ChainMap

# 创建基础两个字典
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

# 创建 chainmap
chain_map = ChainMap(baseline, adjustments)

# 获取chianmap 中的值
print(chain_map["opera"])
print(chain_map["music"])

# 对基础字典进行更新
baseline.update({"aa": "bb"})
adjustments.update({"ff": "fde"})

print(chain_map["aa"])
print(chain_map.get("ff"))

# 对chainmap 更新会更新到它的第一个链上
chain_map.update({"abc": "erf"})

# 一个可以更新的映射列表。这个列表是按照第一次搜索到最后一次搜索的顺序组织的。
# 它是仅有的存储状态，可以被修改。列表最少包含一个映射。
maps = chain_map.maps

# 返回一个新的 ChainMap 类，包含了一个新映射(map)，
# 后面跟随当前实例的全部映射(map)。
# 如果 m 被指定，它就成为不同新的实例，就是在所有映射前加上 m，
# 如果没有指定，就加上一个空字典，这样的话一个 d.new_child() 调用等价于 ChainMap({}, *d.maps) 。
# 这个方法用于创建子上下文，不改变任何父映射的值。
new_child = chain_map.new_child()

new_child1 = chain_map.new_child({"child1": "child1"})


# 属性返回一个新的 ChainMap 包含所有的当前实例的映射，除了第一个。
# 这样可以在搜索的时候跳过第一个映射。
# 使用的场景类似在 nested scopes 嵌套作用域中使用 nonlocal 关键词。
# 用例也可以类比内建函数 super() 。
# 一个 d.parents 的引用等价于 ChainMap(*d.maps[1:])
parents = chain_map.parents


print("end")
