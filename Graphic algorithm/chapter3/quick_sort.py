# 用递归实现快速排序
# 1、如果是空或者只有一个元素，返回数组
# 2、归位后继续对两边进行快排
import random


def quick_sort(li):
    if len(li) < 2:
        return li
    pivot = li[0]
    left = [i for i in li[1:] if i <= pivot]
    right = [i for i in li[1:] if i >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
    # 只有列表才能合并，所以需要写成[pivot]


a = [x for x in range(15)]
random.shuffle(a)
print(a)
print(quick_sort(a))


