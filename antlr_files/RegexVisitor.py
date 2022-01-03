# Generated from E:/RANDOM/WORKSPACE/ANUL3/SEM1/LFA/Tema3/antlr_files\Regex.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#precedence1.
    def visitPrecedence1(self, ctx:RegexParser.Precedence1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#precedence2.
    def visitPrecedence2(self, ctx:RegexParser.Precedence2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#precedence3.
    def visitPrecedence3(self, ctx:RegexParser.Precedence3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#precedence4.
    def visitPrecedence4(self, ctx:RegexParser.Precedence4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#union.
    def visitUnion(self, ctx:RegexParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#concat.
    def visitConcat(self, ctx:RegexParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#kleene.
    def visitKleene(self, ctx:RegexParser.KleeneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#parentheses.
    def visitParentheses(self, ctx:RegexParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#symbol.
    def visitSymbol(self, ctx:RegexParser.SymbolContext):
        return self.visitChildren(ctx)



del RegexParser