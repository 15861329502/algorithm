from python_basic.basic_function import gcd


# 1、定义一个分数类
class Function(object):
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(str(self.num), '/', str(self.den))

    def __str__(self):  # 重写自带的字符串转换函数（默认转换）
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):  # 重写add方法，other参数表示另一个被加的对象
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newden, newnum)
        return Function(newnum // common, newden // common)  # 返回重新构造好的分数，方便之后的打印

    def __eq__(self, other):  # 重写__eq__方法，使得通过值来判断相等（深相等），而不是根据引用
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum


my_function1 = Function(3, 5)
my_function2 = Function(3, 5)
print(my_function1)
print(my_function1 + my_function2)
print(my_function1 == my_function2)
