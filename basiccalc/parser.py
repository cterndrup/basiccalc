from .ast import BExpr, ParanExpr, NumExpr
from .lexer import *

class ParseException(Exception):
    """ An Exception while parsing """
    pass

class ParseError(ParseException):
    """ An error that occurs during parsing """
    def __init__(self, message):
        self.message = message

    def message(self):
        return self.message

class Parser(object):
    """ Recursive descent parser for the basic calculator language """

    def __init__(self):
        super().__init__()

    def eval(self, tokens):
        tokens.reverse()
        return self.__parse(tokens).eval()

    def __parse(self, tokens):
        if len(tokens) == 0:
            return tokens

        expressions = []
        self.__expr(tokens, expressions)
        return expressions[0]

    def __expr(self, tokens, expressions):
        self.__term(tokens, expressions)
        self.__expr_prime(tokens, expressions)

    def __expr_prime(self, tokens, expressions):
        top = None
        try:
            top = tokens[-1]
        except IndexError:
            return
        else:
            if isinstance(top, PlusOp) or isinstance(top, MinusOp):
                op = self.__op1(tokens)
                self.__term(tokens, expressions)
                right = expressions.pop()
                left  = expressions.pop()
                expressions.append(BExpr(left, op, right))

                self.__expr_prime(tokens, expressions)

    def __term(self, tokens, expressions):
        self.__term_prime(tokens, expressions)
        self.__term_dprime(tokens, expressions)

    def __term_prime(self, tokens, expressions):
        if isinstance(tokens[-1], Num):
            expressions.append(self.__num(tokens))
        else:
            e1 = tokens.pop()
            self.__expr(tokens, expressions)
            e3 = tokens.pop()
            expressions.append(ParanExpr(e1, expressions.pop(), e3))

    def __term_dprime(self, tokens, expressions):
        top = None
        try:
            top = tokens[-1]
        except IndexError:
            return
        else:
            if isinstance(top, MultOp) or isinstance(top, DivOp):
                op = self.__op2(tokens)
                self.__term_prime(tokens, expressions)
                right = expressions.pop()
                left  = expressions.pop()
                expressions.append(BExpr(left, op, right))

                self.__term_dprime(tokens, expressions)

    def __op1(self, tokens):
        return tokens.pop()

    def __op2(self, tokens):
        return tokens.pop()

    def __num(self, tokens):
        return NumExpr(tokens.pop())
