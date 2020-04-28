# 堆排序

def buildMaxHeap(lists):
    """
    构造最大堆
    :param lists:
    :return:
    """
    llen = len(lists)
    for i in range(llen >> 1, -1, -1):
        heapify(lists, i, llen)


def heapify(lists, i, llen):
    """
    堆化
    :param lists:
    :param i:
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < llen and lists[left] > largest:
        largest = left
    if right < llen and lists[right] > largest:
        largest = right
    if largest != i :
        swap(lists, i, largest)
        heapify(lists, largest, llen)


def swap(lists, i, j):
    """
    交换列表中的两个元素
    :param lists:
    :param i:
    :param j:
    :return:
    """
    lists[i], lists[j] = lists[j], lists[i]


def heapSort(lists):
    """
    堆排序，从小到大进行排序

    需要构造一个最大堆，然后首位交换，然后lists 的长度-1， 重复这个过程，直至lists中只剩一个元素

    :param lists:
    :return:
    """
    llen = len(lists)
    buildMaxHeap(lists)
    for i in range(len(lists)-1, 0, -1):
        swap(lists, 0, i)
        llen -= 1
        heapify(lists, 0, llen)
    return lists


if __name__ == "__main__":
    arr = [8, 3, 5, 1, 6, 4, 9, 0, 2]
    b = heapSort(arr)
    print(b)
