from src.constant.Constant import Constant
from src.result.Result import Result


class Number(Constant):
    value = -1

    def getValue(self):
        self.value = int(self.string)
        return self.value

    def accept(self,visitor):
        return visitor.visit(self)
