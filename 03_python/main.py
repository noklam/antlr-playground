from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser

code = open('examples/multi-line-imports.py', 'r').read()
codeStream = InputStream(code)
lexer = Python3Lexer(codeStream)

tokens = lexer.getAllTokens()

for t in tokens:
    print(t.text, t.type)