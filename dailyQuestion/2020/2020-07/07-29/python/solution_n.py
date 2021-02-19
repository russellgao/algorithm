
# 一次遍历
def missingNumber(nums: [int]) -> int:
    for i,v in enumerate(nums) :
        if i != v :
            return i
    return nums[-1] + 1

if __name__ == "__main__" :
    nums = [0,1,2,3,4,5,6,7,9]
    result = missingNumber(nums)
    print(result)