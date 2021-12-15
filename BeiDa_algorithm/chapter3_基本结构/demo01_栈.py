# 简单括号匹配
"""
特点：
    1、每个开括号要恰好对应一个闭括号
    2、每对开闭括号要正确的嵌套
思考：
    最后打开的左括号，需要匹配最先遇到的右括号：次序反转，适合用栈
"""
from python_basic.basic_type import Stack


def par_match(in_string):
    s = Stack()  # 定义空栈
    for i in range(len(in_string)):
        if in_string[i] == '(':
            s.push('(')
        else:
            if s.isEmpty():
                return False  # 如果遇到一个不匹配，则直接return
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False


# 判断含有{、[、(的情况
def par_match2(in_string):
    s = Stack()
    matched = True
    for i in range(len(in_string)):
        if in_string[i] in "{[(":
            s.push(in_string[i])
        else:
            if s.isEmpty():
                return False
            else:
                pop_num = s.pop()  # 既pop了，也返回了
                if not is_matched(pop_num, in_string[i]):
                    return False
    if s.isEmpty():
        return True
    return False


def is_matched(str1, str2):
    # 判断两个括号字符是否匹配
    str1s = "{[("
    str2s = "}])"
    # 小技巧，通过索引来判断是否匹配，避免了复杂的if判断语句
    # 要注意传入的顺序
    return str1s.index(str1) == str2s.index(str2)


print(par_match('((()))'))
print(par_match('(()'))
print(par_match2('{{([][])}()}'))
print(par_match2('[{()]'))

# 2、进制转换问题
"""
对于十进制转换成二进制的问题：
    1、除以2，得到的余数，从低位到高维
    2、书写的时候是从左到右：高位到地位
    3、所以有个次序反转的现象：先得到的余数，要在后面写
"""


def dec2bin(in_num):
    remstack = Stack()
    while in_num > 0:
        remstack.push(in_num % 2)
        in_num //= 2
    str_out = ""
    for i in range(remstack.size()):
        str_out += str(remstack.pop())
    return str_out


# 十进制转换成任意进制
def dec2auto(in_num, based):
    digits = "0123456789ABCDE"
    remstack = Stack()
    while in_num > 0:
        remstack.push(in_num % based)
        in_num //= based
    str_out = ""
    for i in range(remstack.size()):
        str_out += digits[remstack.pop()]
    return str_out


print(dec2bin(785))
print(dec2auto(7899, 16))
print(dec2auto(7899, 8))
