from BaseLabel import BaseMDLabel

class Header(BaseMDLabel):
    def __init__(self, text, level:int = 1, info = "This class is a Header "):
        super().__init__(text, info)
        self.level = min(level, 6)

    

    def MDFormatText(self):
        return '#' * self.level + ' ' + self.text + '\n'
    