from syntax.syntax_node import SyntaxNode
from syntax.syntax_type import SyntaxType


class UnarySyntaxNode(SyntaxNode):
    def __init__(self, hierarchy: int, syntax_type: SyntaxType, / , next: SyntaxNode = None) -> None:
        super().__init__(hierarchy, syntax_type)
        self.next = next

    def get_next_node(self) -> SyntaxNode:
        return self.next
    
    def set_next_node(self, syntax_node: SyntaxNode) -> None:
        self.next = syntax_node
    
    def print_self(self, prefix: str, end = False, first = False):
        if first: print(self.syntax_type)
        else:
            print(f"{prefix}{'└─' if end else'├─'}{self.syntax_type}")
            prefix += "  " if end else "│ "
        
        self.next.print_self(prefix, end = True)


    def evaluate(self):
        if self.syntax_type != SyntaxType.BRACKETS:
            print(f"Error: cannot evaluate node of type {self.syntax_type.name}")
            raise Exception()
        
        return self.next.evaluate()