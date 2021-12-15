import math

in_number = float(input("请输入一个非负数："))
if in_number < 0:
    raise RuntimeError("不可以输入一个负数")
else:
    print(math.sqrt(in_number))
print("结束")
