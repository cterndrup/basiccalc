class Token(object):
    """ A token """
    def __init__(self, value):
        self.value = value

    def token(self):
        return self.value

class Num(Token):
    """ An integer """
    def __init__(self, value):
        super().__init__(str(value))

class OpenedParan(Token):
    """ An open parantheses token """
    def __init__(self):
        super().__init__("(")

class ClosedParan(Token):
    """ A closed parantheses token """
    def __init__(self):
        super().__init__(")")

class Op(Token):
    """ An operator from the set { +, -, *, / } """
    def __init__(self, op):
        super().__init__(op)

    def op(self):
        return super().token()

class PlusOp(Op):
    """ The addition operator """
    def __init__(self):
        super().__init__("+")

class MinusOp(Op):
    """ The subtraction operator """
    def __init__(self):
        super().__init__("-")

class MultOp(Op):
    """ The mulitiplication operator """
    def __init__(self):
        super().__init__("*")

class DivOp(Op):
    """ The division operator """
    def __init__(self):
        super().__init__("/")

class Lexer(object):
    """ lexer for the basic calculator language """
    def __init__(self):
        super().__init__()

    def tokenize(self, string):
        isNum  = False
        num    = 0
        tokens = []
        for char in string:
            if char == ' ':
                if isNum:
                    tokens.append(Num(num))
                    num   = 0
                    isNum = False
                continue
            elif char in TOKENS:
                if isNum:
                    tokens.append(Num(num))
                    num   = 0
                    isNum = False
                tokens.append(TOKENS[char])
            else:
                isNum = True
                num   = num*10 + int(char)

        if isNum:
            tokens.append(Num(num))

        return tokens
                
TOKENS = {
    '(':  OpenedParan(),
    ')':  ClosedParan(),
    '+':  PlusOp(),
    '-':  MinusOp(),
    '*':  MultOp(),
    '/':  DivOp()
}
