def is_postorder(nums):
    """

    :param nums:
    :return:
    """
    def recur(i,j) :
        if i >= j :
            return True
        p = i
        while nums[p] < nums[j] :
            p += 1
        m = p
        while nums[p] > nums[j] :
            p += 1
        return p ==j and recur(i,m-1) and recur(m,j-1)
    return recur(0,len(nums)-1)

if __name__ == "__main__" :
    nums = [5,7,6,9,11,10,8]
    result = is_postorder(nums)
    print()
