class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n -1) :
            while len(stack) > 0 and nums[stack[len(stack) -1]] < nums[i %n] :
                res[stack[len(stack) -1]] = nums[i %n]
                stack.pop()
            stack.append( i % n)
        return res

if __name__ == "__main__" :
    s = Solution()
    nums = [1,2,1,7,6,4,9,8,1]
    res = s.nextGreaterElements(nums)
    print(res)