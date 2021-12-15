# 1、使用递归求解列表中数据的和
def sum_re(li):
    if li == []:
        return 0
    return li[0] + sum(li[1:])   # 常用列表中的切片操作


a = [x for x in range(10)]
print(sum_re(a))


# 2、使用递归，计算列表中的元素数
# 1）：基线条件列表中没有数，返回0
# 2）：缩小规模：每次用1+后面的长度
def list_count(li):
    if li == []:
        return 0
    return 1 + list_count(li[1:])


a = [x for x in range(11)]
print(list_count(a))


# 3、使用递归，找出列表中最大的数
def max_list(li):
    if li == []:
        return 0
    elif len(li) == 1:
        return li[0]
    elif len(li) == 2:
        return li[0] if li[0] > li[1] else li[1]
    return li[0] if li[0] > max_list(li[1:]) else max_list(li[1:])


a = [x for x in range(10)]
print(max_list(a))











