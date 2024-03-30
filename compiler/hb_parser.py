from lexer import Lexer

from syntax.abstract_syntax_tree import AbstractSyntaxTree
from syntax.binary_syntax_node import BinarySyntaxNode
from syntax.end_syntax_node import EndSyntaxNode
from syntax.syntax_hierarchy import Hierarchy
from syntax.syntax_token import SyntaxToken
from syntax.syntax_type import SyntaxType
from syntax.unary_syntax_node import UnarySyntaxNode



class Parser:
    lexer: Lexer
    tokens: list[SyntaxToken]

    tree: AbstractSyntaxTree


    def __init__(self, text: str):
        self.lexer = Lexer(text)
        self.tree = AbstractSyntaxTree()


    def parse_tree(self):
        depth = 0

        while (token := self.lexer.next_token()).syntax_type != SyntaxType.EOF:
            syntax_type: SyntaxType = token.syntax_type

            if syntax_type == SyntaxType.WHITE_SPACE: continue

            elif syntax_type == SyntaxType.NUMBER:
                syntax_node = EndSyntaxNode(Hierarchy.NUMBER, syntax_type, token.value)
            
            elif syntax_type == SyntaxType.OPEN_BRACKET:
                self.tree.add_node(depth, UnarySyntaxNode(Hierarchy.BRACKETS, SyntaxType.BRACKETS))
                depth += 1
                continue
            elif syntax_type == SyntaxType.CLOSE_BRACKET:
                depth -= 1
                continue

            elif syntax_type in [SyntaxType.STAR, SyntaxType.SLASH]:
                syntax_node = BinarySyntaxNode(Hierarchy.MULTIPLICATION, syntax_type)

            elif syntax_type in [SyntaxType.PLUS, SyntaxType.MINUS]:
                syntax_node = BinarySyntaxNode(Hierarchy.ADDITION, syntax_type)

            else:
                print("ERROR!")


            self.tree.add_node(depth, syntax_node)


        self.tree.print_self()

        """
        try:
            self.tree.print_self()
        except(Exception):
            pass
            
        print()
        """

    def reset(self, text):
        self.tree = AbstractSyntaxTree()
        self.lexer.reset(text)
        self.parse_tree()
            


'''
def main():
    parser = Parser("")
    while(True):
        text = input(">")
        parser.reset(text)





if __name__ == "__main__":
    main()

'''