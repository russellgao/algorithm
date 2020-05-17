# 有符号数和无符号数举例

import ctypes

num = 17039472050328044269
# num = 90

# 转换成有符号数
a = ctypes.c_int64(num).value

# 转换成无符号数
b = ctypes.c_uint64(a).value

print()
