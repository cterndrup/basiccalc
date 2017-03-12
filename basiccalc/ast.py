# Contains class definitions for expressions in the basic calculator language

OP = {
    "+": lambda a, b: int(a) + int(b),
    "-": lambda a, b: int(a) - int(b),
    "*": lambda a, b: int(a) * int(b),
    "/": lambda a, b: int(a) / int(b)
}

class Expr(object):
    """ Base expression class """
    pass

class ParanExpr(Expr):
    """ (Expr) """
    def __init__(self, opened, expr, closed):
        self.opened  = opened
        self.expr    = expr
        self.closed  = closed

    def eval(self):
        return self.expr.eval()

class BExpr(Expr):
    """ Expr Op Expr """
    def __init__(self, left_expr, op, right_expr):
        self.left_expr = left_expr
        self.op = op
        self.right_expr = right_expr

    def eval(self):
        return OP[self.op.token()](
                    self.left_expr.eval(),
                    self.right_expr.eval()
               )

class NumExpr(Expr):
    """ Integer """
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num.token()
