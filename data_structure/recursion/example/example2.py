
def reverseLists(list1) :
    """
    原地用递归的方法反转list
    :param list1:
    :return:
    """
    def helper(list1,left,right) :
        if left < right :
            list1[left] , list1[right] = list1[right] , list1[left]
            helper(list1,left + 1 , right -1)
    helper(list1,0,len(list1) - 1)

if __name__ == "__main__" :
    list1 = ["a", "b", "c" , "d" , "d","e"]
    reverseLists(list1)
    print()
