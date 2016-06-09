from src.constant.Number import Number
from src.modifier.Modifier import Modifier


class Lowest(Modifier):
    symbol = "L"

    def evaluate(self):
        return self.child.evaluate()

    def validate(self):
        self.child.validate()
        if not isinstance(self.child, Number):
            raise SyntaxError(
                "LOWEST SYNTAX ERROR: Expected number. Got '%s'" % self.child.string)