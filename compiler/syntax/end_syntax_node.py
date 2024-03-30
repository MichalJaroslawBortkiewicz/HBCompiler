from syntax.syntax_node import SyntaxNode
from syntax.syntax_type import SyntaxType

class InvalidFunctionCallException(Exception):
    pass

class EndSyntaxNode(SyntaxNode):
    def __init__(self, hierarchy: int, syntax_type: SyntaxType, value) -> None:
        super().__init__(hierarchy, syntax_type)
        self.value = value
    
    def print_self(self, prefix: str, end = False):
        print(f"{prefix}{'└─' if end else'├─'}{self.syntax_type}: {self.value}")

    
    def get_next_node():
        return None

    def set_next_node():
        raise InvalidFunctionCallException()
    

    def evaluate(self):
        return self.value
