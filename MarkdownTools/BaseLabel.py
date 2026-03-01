class BaseMDLabel:
    """
    作为所有Markdown语法标签的基类
    """

    def __init__(
        self, text: str | None, info: str | None = "This class is a base md label class"
    ):
        self.text: str | None = text
        self.info: str | None = info

    def __str__(self) -> str | None:
        return self.MDFormatText()

    def MDFormatText(self) -> str | None:
        print("This method should be rewrite in child class")
        return None
