# 方法一
def subarraySum1(nums: [int], k: int) -> int:
    """
    枚举
    :param nums:
    :param k:
    :return:
    """
    count = 0
    for i in range(len(nums)) :
        sumn = 0
        for j in range(i,-1,-1) :
            sumn += nums[j]
            if sumn == k :
                count +=1
    return count

# 方法二
def subarraySum2(nums: [int] , k: int) -> int :
    """
    前缀和 + 哈希表优化
    :param nums:
    :param k:
    :return:
    """
    mp = {0: 1}
    count = 0
    pre = 0
    for i in range(len(nums)):
        pre += nums[i]
        count += mp.get(pre - k, 0)
        mp[pre] = mp.get(pre, 0) + 1
    return count

if __name__ == "__main__" :
    nums = [3,4,7,2,-3,1,4,2]
    result = subarraySum2(nums,7)
    print(result)