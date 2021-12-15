# 识别变位词
# 方法1：逐字检查法   O(n^2)
# 输入：两个字符串；输出：False或者True
# 遍历st1中每一个字符，判断是否在str2中有，若有则设为None，没有则直接返回False
def anagram_solution1(str1, str2):
    if len(str1) == len(str2):
        a_list = list(str2)  # 由于字符串是不可变类型，所以需要单独用一个列表存放
        for pos1 in range(len(str1)):
            found = False
            for pos2 in range(len(str2)):
                if a_list[pos2] == str1[pos1]:
                    found = True
                    a_list[pos2] = None
                    break
            if not found:
                return False
        return True
    else:
        return False


# 解法2：排序比较：按照字母排序后判断是否相等即可  复杂度是排序的复杂度
def anagram_solution2(str1, str2):
    a_list, b_list = list(str1), list(str2)  # 不可变类型，仍然要转成列表
    a_list.sort()
    b_list.sort()
    return a_list == b_list


# 解法3：计数比较法：计算出26个字母在两个字符串中出现的次数，存放在两个计数列表中，如果列表相同，则是变位词
# 这种解法，字符串的字符只能是字母，否则无效
# 复杂度：O(n)
def anagram_solution3(str1, str2):
    a, b = [0] * 26, [0] * 26  # 定义两个计数列表
    for i in range(len(str1)):
        pos1 = ord(str1[i]) - ord('a')  # 通过ord函数，返回字母的Unicode编码
        a[pos1] += 1
    for j in range(len(str2)):
        pos2 = ord(str2[j]) - ord('a')
        b[pos2] += 1
    return a == b


# 改进解法3：用字典作为计数器，则无需使用ord
def anagram_solution4(str1, str2):
    a_dict, b_dict = {}, {}
    for i in range(len(str1)):
        if str1[i] in a_dict.keys():
            a_dict[str1[i]] += 1
        else:
            a_dict[str1[i]] = 1
    for j in range(len(str2)):
        if str2[j] in b_dict.keys():
            b_dict[str2[j]] += 1
        else:
            b_dict[str2[j]] = 1
    # print(a_dict, b_dict, sep='\n')
    return a_dict == b_dict


print(anagram_solution1('abcd', 'adbc'))
print(anagram_solution2('python', 'typshon'))
print(anagram_solution3('python', 'typhon'))  # 以空间换取时间（空间和时间之间的取舍）
print(anagram_solution4('abcdeffedcba', 'fedcbaabcdef'))
