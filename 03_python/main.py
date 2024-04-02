from antlr4 import ParseTreeWalker, InputStream, CommonTokenStream
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3ParserListener import Python3ParserListener
from antlr4 import ParseTreeWalker
from Python3ImportParserListener import Python3ImportListener
code = open('examples/multi-line-imports.py', 'r').read()
codeStream = InputStream(code)
lexer = Python3Lexer(codeStream)


# parser = Python3Parser(lexer)
token_stream = CommonTokenStream(lexer)
parser = Python3Parser(token_stream)
listener = Python3ImportListener()
tree = parser.file_input()



tokens = lexer.getAllTokens()
ParseTreeWalker().walk(listener, tree)

# for t in tokens:
    # print(dir(t))
#     # raise
#     print(t)