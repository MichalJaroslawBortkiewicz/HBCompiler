from syntax.syntax_token import SyntaxToken
from syntax.syntax_type import SyntaxType


class Lexer:
    position: int = 0
    text: str
    
    def __init__(self, text: str):
        self.text = text


    def tokenize(self) -> list[SyntaxToken]:
        tokens: list[SyntaxToken] = []

        while (token := self.next_token()).syntax_type != SyntaxType.EOF:
            tokens.append(token)

        return tokens


    def next_token(self) -> SyntaxToken:
        ind = self.position
        self.position += 1

        if(ind >= len(self.text)):
            return SyntaxToken(SyntaxType.EOF, '\0')
        
        if self.text[ind].isspace():

            while ind < len(self.text) and self.text[ind].isspace():
                ind += 1

            self.position = ind
            return SyntaxToken(SyntaxType.WHITE_SPACE, None)
        
        if self.text[ind] == '+':
            return SyntaxToken(SyntaxType.PLUS, '+')
        if self.text[ind] == '-':
            return SyntaxToken(SyntaxType.MINUS, '-')
        if self.text[ind] == '*':
            return SyntaxToken(SyntaxType.STAR, '*')
        if self.text[ind] == '/':
            return SyntaxToken(SyntaxType.SLASH, '/')
        

        if self.text[ind] == '(':
            return SyntaxToken(SyntaxType.OPEN_BRACKET, '()')
        if self.text[ind] == ')':
            return SyntaxToken(SyntaxType.CLOSE_BRACKET, ')')

        if self.text[ind].isdigit():
            number = ""

            while ind < len(self.text) and self.text[ind].isdigit():
                number += self.text[ind]
                ind += 1
            
            self.position = ind

            return SyntaxToken(SyntaxType.NUMBER, int(number))
        
        return SyntaxToken(SyntaxType.BAD_TOKEN, None)
        

    def reset(self, text):
        self.text = text
        self.position = 0