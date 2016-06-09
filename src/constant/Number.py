from src.constant.Constant import Constant


class Number(Constant):
    def evaluate(self):
        return int(self.string)

    def validate(self):
        try:
            int(self.string)
        except ValueError:
            raise SyntaxError("NUMBER SYNTAX ERROR: Expected number without characters but got '%s'"%self.string)
        if int(self.string) <= 0:
            raise ValueError("NUMBER VALUE ERROR: Expected number greater then 0 got '%s'"%self.string)
