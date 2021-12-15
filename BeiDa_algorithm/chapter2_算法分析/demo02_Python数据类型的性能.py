# 1、使用timeit中的Timer模块，测试四种生成列表的性能
from timeit import Timer
import random


def test1():
    l = []
    for i in range(1000):
        l = l + [i]  # 列表的拼接，等价于extend


def test2():
    l = []
    for i in range(1000):
        l.append(i)  # 使用append方法


def test3():
    l = [i for i in range(1000)]  # 使用列表推导式的方法


def test4():
    l = list(range(1000))  # 使用range用list进行转换成列表


t1 = Timer("test1()", "from __main__ import test1")  # 先实例化这个对象
print(f'拼接列表耗时{t1.timeit(number=1000)}秒')  # number表示执行参数

t2 = Timer("test2()", "from __main__ import test2")
print(f'使用append方法耗时{t2.timeit(number=1000)}秒')

t3 = Timer("test3()", "from __main__ import test3")
print(f'使用列表推导式耗时{t3.timeit(number=1000)}秒')

t4 = Timer("test4()", "from __main__ import test4")
print(f'使用range的方法耗时{t4.timeit(number=1000)}秒')

# 2、探究list的不同pop操作计算复杂性
popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")
x = list(range(2000000))  # 长度为两百万的列表
print(f'弹出指定数据用时{popzero.timeit(1000)}秒')
print(f'弹出末尾数据用时{popend.timeit(1000)}秒')

# 看看增长的变化
# print(f'pop()\t\tpop(0)')
# for i in range(1000000, 100000001, 1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print(f'{pt:.8f}\t{pz:.8f}')


# list和dict操作的对比，随机检索出一个值进行计时对比
# 结论：列表的in操作是O(n)，字典的in操作是O(n)
for i in range(10000, 1000001, 20000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f'i: {i}, list_time: {list_time:.5f}, dict_time: {dict_time:.5f}')
