class Solution:
    def canPartition(self, nums: [int]) -> bool:
        n = len(nums)
        if n < 2 :
            return False
        sumn = sum(nums)
        if sumn % 2 != 0 :
            return False
        target = sumn >> 1
        maxn = max(nums)
        if maxn > target :
            return False
        dp = [False] * ( target + 1)
        dp[0] = True
        for i in range(n) :
            v = nums[i]
            for j in range(target, v-1,-1) :
                dp[j] = dp[j] or dp[j-v]
        return dp[target]



if __name__ == "__main__" :
    s = Solution()
    a = s.canPartition([1,2,5])
    print(a)

