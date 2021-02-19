class Solution:
    def __init__(self):

        self.SEG_COUNT = 4
        self.result = []
        self.segments = [0] * self.SEG_COUNT

    def restoreIpAddresses(self, s: str) -> [str]:
        self.dfs(s, 0, 0)
        return self.result

    def dfs(self, s, segId, segStart):
        if segId == self.SEG_COUNT:
            if segStart == len(s):
                ipAddr = ""
                for item in self.segments:
                    ipAddr += str(item)
                    ipAddr += "."
                ipAddr = ipAddr[:len(ipAddr) - 1]
                self.result.append(ipAddr)
            return
        if segStart == len(s):
            return
        if s[segStart] == "0":
            self.segments[segId] = 0
            self.dfs(s, segId + 1, segStart + 1)

        addr = 0
        for i in range(segStart, len(s)):
            addr = addr * 10 + int(s[i])
            if addr > 0 and addr <= 255:
                self.segments[segId] = addr
                self.dfs(s, segId + 1, i + 1)
            else:
                break


if __name__ == "__main__":
    s = "0000"
    solution = Solution()
    result = solution.restoreIpAddresses(s)
    print(result)
