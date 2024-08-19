# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Comp0010ShellParser import Comp0010ShellParser
else:
    from Comp0010ShellParser import Comp0010ShellParser

# This class defines a complete generic visitor for a parse tree produced by Comp0010ShellParser.

class Comp0010ShellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Comp0010ShellParser#command.
    def visitCommand(self, ctx:Comp0010ShellParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#pipe.
    def visitPipe(self, ctx:Comp0010ShellParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#call.
    def visitCall(self, ctx:Comp0010ShellParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#atom.
    def visitAtom(self, ctx:Comp0010ShellParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#argument.
    def visitArgument(self, ctx:Comp0010ShellParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#redirection.
    def visitRedirection(self, ctx:Comp0010ShellParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#quoted.
    def visitQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        return self.visitChildren(ctx)



del Comp0010ShellParser