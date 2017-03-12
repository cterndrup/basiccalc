from basiccalc import lexer, parser

print("PRESS CONTROL+C TO EXIT.")
lexer   = lexer.Lexer()
parser  = parser.Parser()
toks    = []
while True:
    try:
        try:
            print()
            expr = input("Enter an arithmetic expression: ")
            toks = lexer.tokenize(expr)
        except Exception as e:
            print("Invalid expression!")
            print("Expressions may only consist of integers, +, -, / *, (, )")
        else:
            print(parser.eval(toks))
    except KeyboardInterrupt:
        print()
        break
