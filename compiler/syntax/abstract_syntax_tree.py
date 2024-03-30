from syntax.end_syntax_node import EndSyntaxNode
from syntax.syntax_hierarchy import Hierarchy
from syntax.syntax_node import SyntaxNode
from syntax.syntax_type import SyntaxType
from syntax.unary_syntax_node import UnarySyntaxNode

class AbstractSyntaxTree:
    root: UnarySyntaxNode = UnarySyntaxNode(Hierarchy.BRACKETS, SyntaxType.BRACKETS)

    def __init__(self) -> None: pass

    def add_node(self, depth: int, syntax_node: SyntaxNode) -> None:        
        node = self.root
        
        #TODO: fix this - inocorrect depth calculation
        while depth > 0:
            node = node.get_next_node()
            if node.syntax_type == SyntaxType.BRACKETS:
                depth -= 1

        while (node.get_next_node() != None and
               node.get_next_node().hierarchy < syntax_node.hierarchy):
            node = node.get_next_node()


        temp_node = node.get_next_node()

        if temp_node != None:
            syntax_node.left = temp_node
            node.set_next_node(syntax_node)
            return
        
        """
        if syntax_node.syntax_type == SyntaxType.MINUS:
            temp_node = EndSyntaxNode()
        """






        if node.get_next_node() == None:
            node.set_next_node(syntax_node)
            return

        syntax_node.left = node.get_next_node()
        node.set_next_node(syntax_node)

    
    def print_self(self):
        self.root.print_self("", True, True)

    
    def evaluate(self):
        return self.root.evaluate()