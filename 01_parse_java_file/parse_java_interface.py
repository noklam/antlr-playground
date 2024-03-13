from antlr4 import TokenStream, CommonTokenStream, ParseTreeWalker, InputStream
from JavaListener import JavaListener
from JavaParser import JavaParser
from JavaLexer import JavaLexer
import argparse


class ExtractnterfaceListener(JavaListener):
    def __init__(self, parser):
        self.parser = parser

    def enterClassDeclaration(self, ctx):
        print("interface I" + "ctx.Identifier()" + " {")

    def exitClassDeclaration(self, ctx):
        print("}")

    def enterMethodDeclaration(self, ctx):
        print("*****", dir(ctx))
        print(type(ctx))
        tokens = self.parser.getTokenStream()
        token_type = "void"
        if type(ctx) is not None:
            token_type = tokens.getText(*ctx.getSourceInterval())
        # args = tokens.getText(ctx.formalParameters())
        # print("\t" + token_type + " " + ctx.Identifier() + args + ";")
        print("\t"  + " "  + ";")


parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"))
args = parser.parse_args()

text = args.file.read()
print("=== Open File ===")
print(text)
print("=== Close File === ")

lexer = JavaLexer(InputStream(text))
tokens = CommonTokenStream(lexer)
print(tokens)
# raise
parser = JavaParser(tokens)
tree = parser.compilationUnit()  # parse
walker = ParseTreeWalker()
extractor = ExtractnterfaceListener(parser)
walker.walk(extractor, tree)  # initiate walk of tree with listener
