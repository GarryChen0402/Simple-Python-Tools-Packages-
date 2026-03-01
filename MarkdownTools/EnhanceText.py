from BaseLabel import BaseMDLabel

class EnhanceText(BaseMDLabel):
    def __init__(self, text, info = "This class is a enchanced text label class", isBold: bool = False, isItalic: bool = False):
        super().__init__(text, info)
        self.isBold = isBold
        self.isItalic = isItalic

    def MDFormatText(self):
        if self.isBold and not self.isItalic:
            text = f'**{self.text}**'
        elif not self.isBold and self.isItalic:
            text = f'*{self.text}*'
        elif self.isBold and self.isItalic:
            text = f'***{self.text}***'

        return text