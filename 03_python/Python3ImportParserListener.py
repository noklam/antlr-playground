
from Python3ParserListener import Python3ParserListener

class Python3ImportListener(Python3ParserListener):
    # def enterImport_stmt(self,ctx):
    #     print("Enter")
    #     print(ctx.getText())
    #     s = ctx.getText()
    #     print(type(s))


    # def exitImport_stmt(self, ctx):
    #     print("Exit")
    #     print(ctx.getText())

        # ...
    def enterImport_name(self, ctx):
        print("Import_name")
        print("**", ctx.getRuleIndex())
        print(ctx.getText)
        print(ctx.getText())