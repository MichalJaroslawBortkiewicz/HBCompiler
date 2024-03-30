from syntax.abstract_syntax_tree import AbstractSyntaxTree




class Evaluator:
    tree: AbstractSyntaxTree

    def __init__(self, tree: AbstractSyntaxTree) -> None:
        self.tree = tree
    