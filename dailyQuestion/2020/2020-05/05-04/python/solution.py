
def jump(nums) -> int:
    length = len(nums)
    end = 0
    steps = 0
    maxPosition = 0

    for i in range(length - 1) :
        maxPosition = max(maxPosition,i+nums[i])
        if i == end :
            end = maxPosition
            steps += 1
    return steps

if __name__ == "__main__" :
    nums = [2,3,1,1,4]
    steps = jump(nums)
    print(steps)