from syntax.syntax_type import SyntaxType


class SyntaxToken:
    syntax_type: SyntaxType

    def __init__(self, syntax_type: SyntaxType, value: str):
        self.syntax_type = syntax_type
        self.value = value

    
    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        return f"{self.syntax_type.name:15}{self.value}"