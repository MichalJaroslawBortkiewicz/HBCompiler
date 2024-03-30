from syntax.syntax_node import SyntaxNode
from syntax.syntax_type import SyntaxType


class BinarySyntaxNode(SyntaxNode):
    def __init__(self, hierarchy: int, syntax_type: SyntaxType, / , left: SyntaxNode = None, right: SyntaxNode = None) -> None:
        super().__init__(hierarchy, syntax_type)
        self.left = left
        self.right = right


    def get_next_node(self) -> SyntaxNode:
        return self.right
    
    def set_next_node(self, syntax_node: SyntaxNode) -> None:
        self.right = syntax_node
    
    def print_self(self, prefix: str, end = False):
        print(f"{prefix}{'└─' if end else'├─'}{self.syntax_type}")
        prefix += "  " if end else "│ "
        self.left.print_self(prefix)
        self.right.print_self(prefix, end = True) 
    
    def evaluate(self):        
        if self.syntax_type == SyntaxType.PLUS:
            return self.left.evaluate() + self.right.evaluate()
        
        elif self.syntax_type == SyntaxType.MINUS:
            if self.left == None: return -self.right.evaluate()
            return self.left.evaluate() - self.right.evaluate()
        
        elif self.syntax_type == SyntaxType.STAR:
            return self.left.evaluate() * self.right.evaluate()
        
        elif self.syntax_type == SyntaxType.SLASH:
            l_val = self.left.evaluate()
            
            if l_val == 0: raise ZeroDivisionError()
            return l_val / self.right.evaluate()
        
        print(f"Cannot evaluate node of type {self.syntax_type}")
        raise Exception()