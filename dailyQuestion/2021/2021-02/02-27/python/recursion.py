class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        if not s:
            return res
        cnt = [0] * 26
        for item in s:
            cnt[ord(item) - 97] += 1
        split = ""
        for index, item in enumerate(cnt):
            if item > 0 and item < k:
                split = chr(index + 97)
                break
        if split == "":
            return len(s)
        for item in s.split(split):
            res = max(res, self.longestSubstring(item, k))
        return res


if __name__ == "__main__":
    s = "ababbc"
    so = Solution()
    res = so.longestSubstring(s, 2)
    print(res)
