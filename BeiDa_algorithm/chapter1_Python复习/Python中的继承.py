# 以继承的方式构建逻辑门
"""1、首先定义超类LogicGate：
    有一个用于识别的标签，一个输出，
    需要两个方法：用户可以获得逻辑门的标签，知道自己的输出值
"""


class LogicGate:
    def __init__(self, label):
        self.label = label  # 识别自己的标签
        self.output = None  # 自己的输出

    def getLabel(self):
        return self.label  # 可获得自己的标签

    def getOut(self):
        self.output = self.performGateLogic()
        return self.output  # 可获得输出


# 定义两个输入的类BinaryGate（有两个输入pinA和pinB）和一个输入的类UnaryGate（有一个输入pin）
class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)  # 要初始化继承的父类
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input(f'请输入门{self.label}的A引脚的值：'))  # 让用户通过键盘进行输入
        else:
            return self.pinA.getFrom().getOut()

    def getPinB(self):
        if self.pinB == None:
            return int(input(f'请输入门{self.label}的B引脚的值：'))
        else:
            return self.pinB.getFrom().getOut()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("错误：没有可用的引脚!")


class UnaryGate(LogicGate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input(f'请输入门{self.label}的输入：'))
        else:
            return self.pin.getFrom().getOut()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("错误：没有可用的引脚!")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        return 0 if a == 1 else 1


# g1 = AndGate("G1")
# g2 = OrGate("G2")
# g3 = NotGate("G3")
# print(g1.getOut())
# print(g2.getOut())
# print(g3.getOut())
"""
在构建电路前，还需要定义一个Connector类，用于将两个逻辑门联系在一起
包换两个逻辑门实例：fromgate和togate
"""


class Connector:
    def __init__(self, fromgate, togate):
        self.fgate = fromgate
        self.tgate = togate

        togate.setNextPin(self)  # self是Connector，作为参数传给setNextPin

    def getFrom(self):
        return self.fgate

    def getTo(self):
        return self.tgate


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.getOut())
