from syntax.syntax_type import SyntaxType

class SyntaxNode:
    hierarchy: int
    syntax_type: SyntaxType

    def __init__(self, hierarchy: int, syntax_type: SyntaxType) -> None:
        self.syntax_type = syntax_type
        self.hierarchy = hierarchy