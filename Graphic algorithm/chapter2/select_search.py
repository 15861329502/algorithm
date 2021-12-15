# 1、输入：无序数组；输出：有序数组
# 2、每次遍历无序区，将最大的放到最后
# 3、第一层循环，表示选择最大数的趟数，有多少数选择多少趟
# 4、先假定每次最大数都是0，之后循环找出最大数，并且和无序区最后一个数进行交换
import random


def select_search(li):
    """
    :param li: 待排序的无序数组
    :return:  有序数组
    """
    for i in range(len(li) - 1):
        max_index = 0
        for j in range(1, len(li) - i):
            if li[max_index] < li[j]:
                max_index = j
        # 将最大数放到最后
        li[j], li[max_index] = li[max_index], li[j]  # 此时的j就是无序区最后元素的索引
        print(li)
    return li


a = [4, 3, 2, 1, 5, 6, 7, 8, 9]
random.shuffle(a)   # shuffle是在原列表上直接操作，没有返回值，所以不能赋值
select_search(a)
