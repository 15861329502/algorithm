# 1、用low和high两个变量表示两头的数
# 2、mean_index表示中间数的索引
# 3、每次判断mean_index处值的大小和val进行比较，并且进行下一步
# 4、循环条件：low<=high
from time_care import run_time


@run_time
def binary_search(li, val):
    """
    :param li: 输入的有序列表
    :param val: 需要查找的元素
    :return: 需要查找的元素的索引，没有则返回None
    """
    low, high = 0, len(li) - 1
    while low <= high:
        mean_index = (low + high) // 2  # 下表应该是个整数，所以需要整除
        if li[mean_index] > val:
            high = mean_index - 1
        elif li[mean_index] == val:
            return mean_index
        else:
            low = mean_index + 1
    return None


a = [x for x in range(100)]
print(binary_search(a, 1))
