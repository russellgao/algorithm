def minWindow(s: str, t: str) -> str:
    # 初始化两个dict, 一个是t字符串，一个是滑动窗口
    mappings_t = {}
    mappings_windows = {}

    # 初始化t
    for i in range(len(t)):
        if t[i] not in mappings_t:
            mappings_t[t[i]] = 1
        else:
            mappings_t[t[i]] += 1
    i = 0
    # 结果的左右边界
    result_l, result_r = -1, -1
    # 最大的长度
    max_len = float("inf")

    # check 滑动窗口是否包含t
    def check():
        for k, v in mappings_t.items():
            tmp_v = mappings_windows.get(k) or 0
            if tmp_v < v:
                return False
        return True

    # 遍历s 字符串进行检查
    for j in range(len(s)):
        if s[j] in mappings_t:
            tmp = mappings_windows.get(s[j]) or 0
            mappings_windows[s[j]] = tmp + 1
        while check() and i <= j:
            # 更新结果的左右边界
            if j - i + 1 < max_len:
                max_len = j - i + 1
                result_l, result_r = i, j
            # 尝试更新滑动窗口的左边界
            if s[i] in mappings_t:
                mappings_windows[s[i]] -= 1
            i += 1
    if result_r == -1:
        return ""
    return s[result_l:result_r + 1]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    result = minWindow(s, t)

    print(result)
