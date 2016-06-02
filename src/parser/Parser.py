from src.parser.PartFactory import PartFactory


class Parser:
    root = None

    def parse(self,string):
        self.root = PartFactory.fetch_part(string)

    def roll(self):
        return self.root.evaluate()