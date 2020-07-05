
def adfdtest(num: str, k: int) :
    n = len(num)
    nums = [num[i] for i in range(n)]
    count = 0
    flag = True
    for j in range(n):
        if not flag:
            break
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                count += 1
            if count == k:
                flag = False
                break

    return "".join(nums)

if __name__ == "__main__" :
    num = "9438957234785635408"
    k = 23
    result = adfdtest(num,k)
    print(result)
