class Stack():
    """
使用列表来定义栈，默认列表的末尾是栈顶，这样方便append和pop操作

数据项的加入和移除仅发生在同一端
后进先出(LIFO)  Last in First out

举例：浏览器中的后退按钮；word中的撤销操作

栈的操作：
    Stack()：创建一个空栈，不包含任何数据项
    push(item)：将item加入栈，无返回值
    pop()：将栈顶数据移除，并且返回，栈被修改
    peek()："窥视"栈顶数据项，并且返回，栈没有被修改
    isEmpty()：判断栈是否为空栈
    size()：返回栈中有多少个数据项
    """
    def __init__(self):
        self.items = []  # 初始化定义为一个空列表

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
