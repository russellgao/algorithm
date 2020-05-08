
def fastest_path(nums) :
    """
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        len_i = len(nums[i])
        for j in range(len_i):
            if j == 0 :
                nums[i][j] = nums[i - 1][j] + nums[i][j]
            elif j == len_i-1:
                nums[i][j] = nums[i - 1][j - 1] + nums[i][j]
            else :
                tmp = max(nums[i][j] + nums[i - 1][j - 1], nums[i][j] + nums[i - 1][j])
                nums[i][j] = tmp
    result = max(nums[len(nums) - 1])
    return result

if __name__ == "__main__" :
    nums = [
[7],
[3, 8 ] ,
[8, 1, 0 ],
[2, 7, 4, 4 ],
[4 ,5 ,2, 6, 5]]
    result = fastest_path(nums)
    print(result)