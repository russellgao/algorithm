
from collections import defaultdict



# class collections.defaultdict([default_factory[, ...]])
# 返回一个新的类似字典的对象。 defaultdict 是内置 dict 类的子类。
# 它重载了一个方法并添加了一个可写的实例变量。其余的功能与 dict 类相同，此处不再重复说明。

# 本对象包含一个名为 default_factory 的属性，构造时，第一个参数用于为该属性提供初始值，默认为 None。
# 所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。


# __missing__(key)
# 如果 default_factory 属性为 None，则调用本方法会抛出 KeyError 异常，附带参数 key。

# 如果 default_factory 不为 None，则它会被（不带参数地）调用来为 key 提供一个默认值，
# 这个值和 key 作为一对键值对被插入到字典中，并作为本方法的返回值返回。

# 如果调用 default_factory 时抛出了异常，这个异常会原封不动地向外层传递。

# 在无法找到所需键值时，本方法会被 dict 中的 __getitem__() 方法调用。
# 无论本方法返回了值还是抛出了异常，都会被 __getitem__() 传递。

# 注意，__missing__() 不会 被 __getitem__() 以外的其他方法调用。
# 意味着 get() 会像正常的 dict 那样返回 None，而不是使用 default_factory。

# default_factory
# 本属性由 __missing__() 方法来调用。如果构造对象时提供了第一个参数，则本属性会被初始化成那个参数，
# 如果未提供第一个参数，则本属性为 None。


# ================================================================
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d1 = defaultdict()
d1.default_factory = list

# 下面这个写法和上面两行写法类似
# d1.default_factory(list)

for k,v in s :
    d1[k].append(v)

# a3 不在d1 中，会调用 default_factory 方法初始化a3并且插入到d1中

d1.__missing__("a3")

print(d1)

# ================================================================
s2 = ["b1","b2","b3"]
d2 = defaultdict(int, a1=1,a2=4)
for i in s2 :
    d2.__missing__(i)

print(d2)

# ================================================================
# default_factory 为自定义的lambda 函数
s3 = ["b1","b2","b3"]
d2 = defaultdict(lambda : 4, a1=1,a2=4)
for i in s2 :
    d2.__missing__(i)

print(d2)

# ================================================================

